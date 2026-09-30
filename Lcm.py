def find_lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
a=int(input("enter first number"))
b=int(input("enter second number"))
print("LCM is:",find_lcm(a,b))