import expense

filename = input("Enter file name: ")

mode = input("Create new entry or read old? (New/Old): ")

file = open(filename, 'a+')

entry = {}

if (mode == "N" or mode == "New"):
    entry["category"] = input("Type expense category: ")
    entry["expense"] = input("Type expense amount: ")
    expense.expense_write(file, entry)
#else:
#    mode = input("Filter by date or category? (D/C): ")
#    if (mode == "D"):
#        day = input("Enter date (YYYY-MM-DD): ")
#    file.seek(0)
#    diary.diary_read(file, day)

file.close()