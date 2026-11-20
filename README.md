# CCC Pipeline Tools

## What it does
Helps me identify overdue follow-ups, count contacts,
identify duplicates, and plan follow-up dates around
weekends and holidays. Follow-ups are due after seven days.

## How to run it
Python 3 is required. Open the project's Codespace
and enter the following command in the terminal:

```bash
python3 follow_up_finder.py
```

The script automatically reads sample_contacts.csv.
It uses November 17, 2026, as a fixed date for testing.
An internet connection is needed to check holidays.

## What it does not do
It doesn't send messages, contact people, connect
to LinkedIn, or modify CRM records.


## Privacy
The project uses fictional contact information for
testing. The .gitignore file keeps untracked files
in the private folder out of Git.