from datetime import date

def diary_write(file, entry):
    file.write(str(date.today()) + " : " + entry + "\n")

def diary_read(file, date):
    lines = file.readlines()
    for row in lines:
        if row.find(date) != -1:
            print(row)