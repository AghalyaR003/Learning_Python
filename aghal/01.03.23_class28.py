# def demo():
#     for i in range(5):
#         return i*i
# print(demo())


# def demo():
#     for i in range(5):
#         yield i*i
# for i in demo():
#     print(i)

# def fun1(list1):
#     for i in range(len(list1)):
#         print(list1[i]*list1[i])
# fun1([7,4,2,9])

# def fun1(list1):
#     list2=[]
#     for i in range(len(list1)):
#         list2.append(list1[i]*list1[i])
#     return list2
# print(fun1([6,5,4,3]))

# def fun1(list1):
#
#     for i in range(len(list1)):
#         yield list1[i]*list1[i]
#
#
# ans=fun1([6,5,7,9])
# for i in ans:
#     print(i)


#elements point method
# list1=[9,8,6,4]
# for i in range(len(list1)):
#     print(list1[i])
#
#
# #index point method
# list1=[9,5,8]
# for i in list1:
#     print(i)

#TYPE OF ARGUMENT

#1 POSITION ARGUMENT
# def add(a,b):
#     print(a+b)
# add(8,5)

#2 keyword argument

# def fun1(name,age):
#     print('name',name,"age",age)
# fun1(age=20,name='aghal')

# #3 default argument
# def fun1(name,age=25):
#     print('name',name,'age',age)
# fun1(name="aghal",age=30)

#4 variable length argument
# def fun1(a,b,*c):
#     print(a,b,c)
# fun1(7,4,9,2,6)

# def fun1(a,b):
#     ans=a+b
#     print(ans)
#     return ans
# ans=fun1(6,4)
# print(ans)

#assignment
# def ShowEmployee(name,salary=12000):
#     print("name",name,"salary",salary)
# ShowEmployee('Ben')
# ShowEmployee(name='Jessa',salary=9000)

#return both add & sub

# def calculation(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub
# res=calculation(40,10)
# print(res)

#variable length arguments
def demo(a,*b):
    print('printing values',a)
    for i in b:
        print(i)
demo(20,40,60)
demo(80,100)
