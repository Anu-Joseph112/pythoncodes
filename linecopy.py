f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")

lines = f1.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        f2.write(lines[i])

f1.close()
f2.close()

print("Odd lines copied successfully")
