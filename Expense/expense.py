from datetime import date, datetime
import json
from pathlib import Path
import csv

def expense_write(filename, entry):
    entry["date"] = date.today().strftime("%Y-%m-%d")
    if Path(filename).exists():
        with open(filename, "r+") as file:
            data = json.load(file)
            data["expenses"].append(entry)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    else:
        with open(filename, "w") as file:
            json.dump({"expenses": [entry]}, file, indent=4)

def expense_read(filename, time1, time2, category):
    export = input("Export to CSV? (Y/N): ")
    with open(filename, "r") as file:
        data = json.load(file)
        
        if (export == "Y"):
            export_data = open("csv_export.csv", "w")
            writer = csv.writer(export_data)
            row = 0
            for entry in data["expenses"]:
                if row == 0:
                    headers = entry.keys()
                    writer.writerow(headers)
                    row += 1
                
                writer.writerow(entry.values())
            export_data.close()
        
        
        for expense in data["expenses"]:
            if (category == ""):
                if (datetime.strptime(expense["date"], "%Y-%m-%d") >= time1 and datetime.strptime(expense["date"], "%Y-%m-%d") <= time2):
                    print(expense)
            else:
                if (datetime.strptime(expense["date"], "%Y-%m-%d") >= time1 and datetime.strptime(expense["date"], "%Y-%m-%d") <= time2 and expense["category"] == category):
                    print(expense)