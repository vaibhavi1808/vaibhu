class parent:
    def fun1(self):
        print("parent")
class son1(parent):
    def son1(self):
        print("child")
class son2(parent):
    def son2(self):
        print("child2") 
obj1=son1()
obj1.fun1()
obj1.son1()
obj2=son2()
obj2.fun1()
obj2.son2()                
