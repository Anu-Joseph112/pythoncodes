list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print("the first list is"+str(list1))
print("the second list is"+str(list2))
# a=len(list1)
# b=len(list2)
# print("length of list1 is",a,"and length of list2 is",b)
# if a==b:
#     print(" the lists are same length")
# else:
#     print(" the lists are different length")
sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("the sum of all element in given list1:",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("the sum of all element in given list2:",sum2)
if sum1==sum2:
    print("list sum to same value")
else:
    print("list sum to different value")
