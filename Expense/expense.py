from datetime import date
import json

def expense_write(file, entry):
    entry["date"] = date.today().strftime("%Y-%m-%d")
    file.write(json.dumps(entry))

def expense_read(file, date):
    lines = file.readlines()
    for row in lines:
        if row.find(date) != -1:
            print(row)