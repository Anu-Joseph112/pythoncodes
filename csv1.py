import csv

f = open("student.csv", "r")

reader = csv.reader(f)

for row in reader:
    if len(row) > 1:
        print(row[1])

f.close()
