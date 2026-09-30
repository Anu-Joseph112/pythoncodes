a=int(input("enter a number:"))
b=int(input("enter another number:"))
print("enter your choice \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("enter your choice:"))
if choice==1:
    print("sum=",a+b)
elif choice==2:
    print("subtraction=",a-b)
elif choice==3:
    print("multiplication=",a*b)
elif choice==4:
    print("division=",a/b)
else:
    print("enter a valid choice")