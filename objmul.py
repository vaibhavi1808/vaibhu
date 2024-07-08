class parent:
    
    def fun1(self):
        print("parent 1")
class parent1(parent):
    def fun2(self):
        print("parent 2") 
class parent2(parent1):
    def fun3(self):
        print("parent 3") 
obj=parent2()
obj=fun1()
obj=fun2()              

