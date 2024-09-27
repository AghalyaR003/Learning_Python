#global
# def fun1():
#     global num1
#     num1=80
#     print(num1)
# num1=70
# fun1()
# print(num1)

#local
# def fun1():
#     num1=70
#     print(num1)
#     return num1
# num1=fun1()
# print(num1)

#GLOBAL
#
# def outer_fn():
#     global num1
#     num1=100
#     print('inside of outer before call',num1)
#     def inner_fn():
#         global num1
#         num1=90
#         print('inside of inner',num1)
#     inner_fn()
#     print('inside of outer after call',num1)
# num1=80
# outer_fn()
# print('outside',num1)

#NONLOCAL

# def outer_fn():
#
#     num1=100
#     print('inside of outer before call',num1)
#     def inner_fn():
#         nonlocal num1
#         num1=90
#         print('inside of inner',num1)
#     inner_fn()
#     print('inside of outer after call',num1)
# num1=80
# outer_fn()
# print('outside',num1)
#
# list1=[8,7,9,4]
# list1[1]=70
# print(list1)


# list1=[8,7,9,4]
# for i in range(len(list1)):
#        list1[i] = 70
# print(list1)

# list1=[8,7,9,4]
# for i in range(len(list1)):
#        list1[i]=list1[i]+100
# print(list1)

list1=[8,7,9,4]
for i in range(len(list1)):
       if i%2==0:
              list1[i] = list1[i] + 100

print(list1)