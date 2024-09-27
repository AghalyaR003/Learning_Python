#SUPER METHOD


# class A:
#     def __init__(self,len,bre):
#         self.len=len
#         self.bre=bre
#     def area(self):
#         print(self.len*self.bre)
# class B(A):
#     def __init__(self,len,bre,hei):
#         super().__init__(len,bre)
#         self.hei=hei
#
#     def cube(self):
#         # ans=A.area(self)
#         print(self.len*self.bre*self.hei)
# obj1=B(8,5,9)
# obj1.cube()


# class A:
#     def __init__(self,len,bre):
#         self.len=len
#         self.bre=bre
#     def area(self):
#         print(self.len*self.bre)
#     def __del__(self):
#         print('height')
# obj1=A(4,5)
# obj1.area()
# del obj1

#MULTILEVEL INHERITANCE

# class A:
#     def __init__(self,len,bre):
#         self.len=len
#         self.bre=bre
#     def area(self):
#         print(self.len*self.bre)
# class B(A):
#     pass
# class C(B):
#     pass
# obj1=C(4,6)
# obj1.area()


# class A:
#     def __init__(self,len,bre):
#         self.len=len
#         self.bre=bre
#     def area(self):
#         print(self.len*self.bre)
# class B(A):
#     pass
# class C(B):
#     pass
# obj1=C(4,6)
# obj1.area()



# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def eat(self):
#         print('eating')
# class DOG(A):
#     def bark(self):
#         print('barking')
# class DOGCHILD(DOG):
#     def fight(self):
#         print('fighting')
# obj1=DOGCHILD(3,5)
# obj1.eat()
# obj1.bark()
# obj1.fight()