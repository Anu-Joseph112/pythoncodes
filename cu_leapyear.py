y=int(input("enter final year:"))
print("future leap years from 2026:")
for x in range(2026,y+1):
    if(x%4==0 and x%100!=0 or x%400==0):
        print(x)
