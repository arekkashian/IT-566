import diary

filename = input("Enter file name: ")

mode = input("Create new entry or read old? (New/Old): ")

file = open(filename, 'a+')

if (mode == "N" or mode == "New"):
    entry = input("Type entry: ")
    diary.diary_write(file, entry)
else:
    day = input("Enter date (YYYY-MM-DD): ")
    file.seek(0)
    diary.diary_read(file, day)

file.close()