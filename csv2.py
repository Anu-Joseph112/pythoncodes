import csv

# Dictionary
data = [
    {'Rollno': 1, 'Name': 'Anu', 'Mark': 90},
    {'Rollno': 2, 'Name': 'Manu', 'Mark': 85},
    {'Rollno': 3, 'Name': 'Amal', 'Mark': 95}
]

# Writing dictionary to CSV file
f = open("student.csv", "w", newline="")

writer = csv.DictWriter(f, fieldnames=['Rollno', 'Name', 'Mark'])

writer.writeheader()
writer.writerows(data)

f.close()

# Reading CSV file
f = open("student.csv", "r")

reader = csv.DictReader(f)

print("Contents of CSV file:")

for row in reader:
    print(row)

f.close()
