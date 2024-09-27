# def fun1():
#     print('enter 2 values')
#
#     n1,n2=map(int,input().split())
#     ans=n1+n2
#     print(ans)
# fun1()
#
#
# def fun1(n1,n2):
#     ans = n1 + n2
#     print(ans)
# print('enter 2 values')
# n1,n2=map(int,input().split())
# fun1(n1,n2)

# def fun(n1,n2):
#     ans=n1+n2
#     print(ans)
#     return ans
# def fun2():
#     print("enter 3 values")
#     n1,n2,n3=map(int,input().split())
#     ans1=fun(n1,n2)*1000
#     print(ans1)
# fun2()

# def fun1(age):
#     ans = age
#     print(ans)
#     return ans
# def fun2():
#     print("enter 2 values")
#     name = input().split()
#     age = map(int, input().split())
#     ans=fun1(age)
#
#     ans1=ans>20
#     print(ans1)
# fun2()
#
# def fun1(name,age):
#     return name,age
# def fun2():
#     print("enter 2 values")
#     name = input().split()
#     age= map(int, input().split())
#     ans1=fun1(name,age)>20
#
#
#     print(ans1)
# fun2()

# def fun1(num1,num2):
#     add=num1+num2
#     sub=num1-num2
#     return add,sub
# add,sub=fun1(13,14)
# print("add is",add,"sub is",sub)

# def demo():
#     print("enter the elements")
#     list1=list(map(int,input().split()))
#     for i in range(len(list1)):
#         if list1[i]%2==0:
#             print(list1[i])
# demo()

def demo(list1):
    for i in range(len(list1)):
        if list1[i]%2==0:
            print(list1[i])
def fun1():
    print("enter the elements")
    list1=list(map(int,input().split()))
    demo(list1)
fun1()






