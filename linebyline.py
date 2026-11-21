f = open("sample.txt", "r")

list1 = []

for line in f:
    list1.append(line)

print("List of lines:")
print(list1)

f.close()
