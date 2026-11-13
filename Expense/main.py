import expense
from datetime import date, datetime

filename = input("Enter file name: ")

mode = input("Create new entry or read old? (New/Old): ")

entry = {}


if (mode == "N" or mode == "New"):
    entry["category"] = input("Type expense category: ")
    entry["expense"] = input("Type expense amount: ")
    expense.expense_write(filename, entry)
else:
    time1 = input("Filter by date range, enter earlier date or none (YYYY-MM-DD): ")
    if (time1 == ""):
        time1 = datetime.min
    else:
        time1 = datetime.strptime(time1, "%Y-%m-%d")
    time2 = input("Enter end date or none (YYYY-MM-DD): ")
    if (time2 == ""):
        time2 = datetime.max
    else:
        time2 = datetime.strptime(time2, "%Y-%m-%d")
    category = input("Enter category to filter by, or none: ")
    
    expense.expense_read(filename, time1, time2, category)