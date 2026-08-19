#abstract method task
from abc import ABC,abstractmethod
class GrandParent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @abstractmethod
    def add(self,):
        pass
    def seb(self,):
        pass 
class parent(GrandParent):
    def add(self,):
        print(self.a+self.b)
    def sub(self,):
        print(self.a-self.b)
    def mul(self,):
        print(self.a*self.b)
    def dev(self,):
        print(self.a/self.b)
a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
obj=parent(a,b)
obj.add()
obj.sub()
obj.mul()
obj.dev()
                