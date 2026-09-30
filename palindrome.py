n=int(input("enter number:"))
rev=0
temp=n
while temp>0:
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10

print(rev)
if n==rev:
    print("is palindrome")
else:
    print("is not palindrome")