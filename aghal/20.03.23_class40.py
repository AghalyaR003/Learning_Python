# class A:
#     def show(self):
#         print('hi')
# class B:
#     def show(self):
#         print('hello')
# class C(B,A):
#     pass
# obj1=C()
# obj1.show()

# class A:
#     def show(self,a,b):
#         print(a+b,a-b)
# class B:
#     def show(self,a,b):
#         print(a*b,a//b)
# class C(B,A):
#     def show(self,a,b):
#         A.show(self,a,b)
#         B.show(self,a,b)
#
#         print('class c')
# obj1=C()
# obj1.show(2,6)

#
# class A:
#     def __init__(self):
#         print('hi A')
# class B:
#     def __init__(self):
#         print('hi B')
# class C(B,A):
#     def __init__(self):
#         # A.show(self,a,b)
#         # B.show(self,a,b)
#
#         print('hi c')
# obj1=C()


#
# class A:
#     def __init__(self):
#         print('hi A')
# class B:
#     def __init__(self):
#         print('hi B')
# class C(B,A):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#
#         print('hi c')
# obj1=C()

#POLYMORPHISM

#METHOD OVERRIDING

#
# class A:
#     def __init__(self):
#         print('hi A')
#
#     def __init__(self,a):
#         print('hi a')
#     def __init__(self,a,b):
#         print('hi',a+b)
# obj1=A(4,7)


# class A:
#     def show(self):
#         print('hi A')
# class B(A):
#     def show(self):
#         print('hi B')
# obj1=B()
# obj1.show()

#class bank:
#    def getroi(self):
#        return 10
#class SBI(bank):
#     def getroi(self):
#         return 15
#class canara(bank):
#     def getroi(self):
#         return 20

#obj1=SBI()
#print(obj1.getroi())
#obj1=canara()
#print(obj1.getroi())











#class Vehicle:
#    def __init__(self,max_speed,mileage,max_capacity):
#        self.max_speed=max_speed
#        self.mileage=mileage
#        self.max_capacity=max_capacity

#    def fare(self):
#        ans=self.max_capacity*100
#        print(ans)
#        return ans
#class bus(Vehicle):
#    def fare(self):
#        ans=Vehicle.fare(self)
#        print(ans*0.1+ans)
#obj1=bus(56,43,500)
#obj1.fare()







