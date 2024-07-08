class parent:
    def fun1(self):
        self.a=10
        print("this parent is in function 1")
class child(parent):
    def fun2(self):
        self.b=20
        print("this is in function 2")
        print("Addition=",self.a+self.b)
obj=child()                
obj.fun1()
obj.fun2()