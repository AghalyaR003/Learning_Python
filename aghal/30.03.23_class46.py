#def outer():
#     def inner():
#         print("hello")
#     inner()
#outer()

#def outer(a,b):
#    def inner():
#        print(a+b)
#    inner()
#print("enter the 2 values")
#a,b=map(int,input().split())
#outer(a,b)

#def outer():
#    def inner():
#        print("hi mam")
#    return inner
#new_fun=outer()
#new_fun()
#del outer
#new_fun()


#def fun1():
#     print("hi")
#def outer(fun1):
#     def inner():
#         fun1()
#         print("hello")
#         print('decorated')
#     return inner
#new_fun=outer(fun1)
#new_fun()
#fun1()


def fun():
    print("hi")
def outer(fun1):
    def inner():
        fun1()
        print("hello")
    return inner()
new_fun=outer(fun)
new_fun()