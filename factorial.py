num=int(input("Enter any number:"))
fact=1
for i in range(1,num+1):
    print(fact,"*",i,"=",fact*i)
    fact=fact*i
print("factorial of",num,"is",fact)