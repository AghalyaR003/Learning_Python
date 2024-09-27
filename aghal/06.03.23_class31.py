#FILTER METHOD


#list1=[9,6,1,4]
# new_list=list(filter(lambda X:X%2==0,list1))
# print(new_list)

# l1=[8,5,3,9]
# l2=[6,5,7,9]
# new_list=list(map(lambda X,Y:X==Y,l1,l2))
#
# count=0
# for i in new_list:
#     if i==True:
#         count=count+1
# print(count)

#REDUCE METHOD

# from functools import reduce
#
# list1=[7,9,4,2]
# def fun1(a,b):
#     return a+b
# ans=reduce(fun1,list1)
# print(ans)


#RECURSIVE METHOD
# def fun1(count):
#     print('hi')
#     count=count+1
#     if count<5:
#         fun1(count)
# count=0
# fun1(count)


# def fact(num):
#     if num==1:
#         return 1
#     else:
#         return num*fact(num-1)
# ans=fact(5)
# print(ans)

#ASSIGNMENT

# list1=[30,10,22,95]
# new_list=list(filter(lambda X:X>=18,list1))
# print(new_list)

# list1=[8,4,6,2]
# list2=[4,7,2,9]
# list3=list(map(lambda X,Y:X*Y,list1,list2))
# print(list3)
# for i in range(len(list3)):
#     list3[i]=list3[i]//2
# print(list3)