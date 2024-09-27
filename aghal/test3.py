#class student():
#    def __init__(self,name,rollno):
#        self.name=name
#        self.rollno=rollno
#    def set_password(self,password):
#        self.__password=password
#    def Show(self):
#          print("name",self.name,"Rollno",self.rollno)
#    def get_password(self):
#        return self.__password
#obj1=student("ACHU","103")
#obj1.set_password("@6374")
#obj1.Show()
#ans=obj1.get_password()
#print(ans)

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def a_method(self):
        print("This is constructor of abstract class")
    def a_method(self):
        print("This is a normal method of abstract class")
class B(A):
    def a_method(self):
        print("This is abstract method")
obj1=B()
obj1.a_method()









 #   def __init__(self):
#        self.count=5
#        self.count=count+1
##obj1=A()
#obj2=A(102)
#print(obj1.count)
#print(obj2.count)