# I am using the example numbers provided in Lab 21
import math 

outreach = 214
connected = 82
info_interview = 0
thanked = 5
champion = 0

# Add up how many people reached each stage.
reached_outreach = outreach + connected + info_interview + thanked + champion
reached_connected = connected + info_interview + thanked + champion
reached_interview = info_interview + thanked + champion
reached_thanked = thanked + champion

# Show my pipeline totals and conversion rates.
print("Reached Outreach:", reached_outreach)
print("Connect rate:", round(reached_connected / reached_outreach * 100), "percent")
print("Conversation rate:", round(reached_interview / reached_connected * 100), "percent")
if reached_interview > 0:
    print("Thank-you rate:", round(reached_thanked / reached_interview * 100), "percent")

    # Calculate how many more people I need to reach 400.
goal = 400
if reached_outreach >= goal:
    print("You are at", goal, "or more.")
else:
    to_go = goal - reached_outreach
    print("To go:", to_go, "more, about", math.ceil(to_go / 15), "labs at 15 a lab.")

    # Check who needs a follow-up based on the 7-day rule.
days_since_last_touch = [2, 9, 6, 7, 12]
for days in days_since_last_touch:
    if days >= 7:
        print(days, "days: follow up today")
    else:
        print(days, "days: not yet")