class mother:
    def fun1(self):
        self.mname="MANISHA"
        self.mage="30"
        print("Name=",self.mname)
        print("Age=",self.mage)

class father(mother):
    def fun2(self):
        self.fname="VISHWAS" 
        self.fage="50"
        print(" Father name=",self.fname)
        print("Father age=",self.fage)       
        
class son(father):
    def fun3(self):
        print(f"name={self.fname},age={self.fage}")

obj=son()
obj.fun1()
obj.fun2()
obj.fun3()
