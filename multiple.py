class student:
    def fun1(self):
        self.roll_no="22"
        self.name="vaibhavi"
        print("roll number=",self.roll_no)   
        print("name=",self.name)

class student1:
    def fun2(self):
        self.age="20"
        print("Age=",self.age)

class student2(student,student1):
    def fun3(self):
        print(f"roll_no={self.roll_no},name={self.name},age={self.age}")

s1=student2()
s1.fun1()
s1.fun2()
s1.fun3()        