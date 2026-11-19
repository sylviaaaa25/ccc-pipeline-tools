import csv
import json
import urllib.error
import urllib.request
from datetime import date, timedelta

FILE = "sample_contacts.csv"
TODAY = date(2026, 11, 17)

def get_holidays(year, country="US"):
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            print("Status:", response.status)
            data = json.load(response)
    except urllib.error.HTTPError as error:
        print("The holiday service answered with status", error.code, "so the holiday check is skipped.")
        return {}
    except (urllib.error.URLError, TimeoutError):
        print("Could not reach the holiday service, so the holiday check is skipped.")
        return {}
    except ValueError:
        print("The answer was not the JSON we expected, so the holiday check is skipped.")
        return {}
    holidays = {}
    for item in data:
        if item["global"]:
            holidays[item["date"]] = item["name"]
    return holidays


def touch_by(last_touch, holidays):
    day = last_touch + timedelta(days=7)
    while day.weekday() >= 5 or day.isoformat() in holidays:
        day = day - timedelta(days=1)
    return day



counts = {}
seen = set()
rows_seen = set()
duplicates = []
skipped = 0
due = []
not_due = []
stage_counts = {}

with open(FILE, newline="") as f:
       for row in csv.DictReader(f):
        name = row["first_name"].strip()
        company = row["company"].strip()
        stage = row["stage"].strip().title()

        if stage == "":
            skipped += 1
            continue

        key = (name.lower(), company.lower())

        if key in seen:
            duplicates.append(name)
        

        seen.add(key)  
        row_key = key + (stage, row["last_activity"].strip())
        if row_key in rows_seen:
            continue
        rows_seen.add(row_key)
        
        stage_counts[stage] = stage_counts.get(stage, 0) + 1

        last_activity = row["last_activity"].strip()

        if last_activity == "":
            continue

        last_date = date.fromisoformat(last_activity)
        days = (TODAY - last_date).days 
        if stage in ["Outreach", "Connected"]:
            if days >= 7:
                due.append((name, company, days))
            else:
                not_due.append((last_date, name, company, stage))
holidays = get_holidays(2026)
due.sort(key=lambda item: item[2], reverse=True)
print("Follow-ups due:")
for name, company, days in due:
    print(name, "-", company, "-", days, "days")

print("Duplicates:", duplicates)
print("Skipped, no stage:", skipped)
print("Total follow-ups due:", len(due)) 

print("Stage counts:")
for stage, count in stage_counts.items():
    print(stage, ":", count)

print("Not due yet, with a suggested touch-by date:")
for last_touch, name, company, stage in sorted(not_due):
    print(" ", name, "at", company, "|", stage, "| touch by", touch_by(last_touch, holidays).strftime("%a, %b %d"))