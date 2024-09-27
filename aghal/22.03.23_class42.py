# from abc import ABC,abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
# class B(A):
#     def add(self):
#         print('add')
#
#     def sub(self):
#         print('sub')
# obj1=B()
# obj1.sub()



from abc import ABC,abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
# class B(A):
#     def add(self):
#         print('add')
# class C(B):
#
#     def sub(self):
#         print('sub')
# obj1=C()
# obj1.add()

# sample_dict={'name':'aa','age':20,'salary':30000,' city':'cbe'}
# dict1={}
# keys=['name','age']
# for i in keys:
#     dict1[i]=sample_dict[i]
# print(dict1)


# from abc import ABC,abstractmethod
#
# class parent(ABC):
#     @abstractmethod
#     def message(self):
#         pass
# class child1(parent):
#     def message(self):
#         print("this is first subclass")
# class child2(parent):
#     def message(self):
#         print("this is second subclass")
#
#
# obj1=child1()
# obj1.message()
# obj2=child2()
# obj2.message()