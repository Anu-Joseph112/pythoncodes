num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    a=temp%10
    sum=sum+a**3
    b=a*a*a
    sum=sum+b
    temp=temp//10
    if num==sum:
        print("armstrong")
    else:
        print("not an armstrong")