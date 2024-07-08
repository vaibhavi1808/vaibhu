class A:
    def getdata(self):
        self.a=int(input("Enter the value of a="))
       
class B(A):
    def putdata(self):
        self.b=int(input("Enter the value of b="))
        
        print("Addition=",self.a+self.b)
        print("substraction=",self.a-self.b)
        print("Multiplication=",self.a*self.b)
        print("Division=",self.a/self.b)
obj1=B()
obj1.getdata()
obj1.putdata()        