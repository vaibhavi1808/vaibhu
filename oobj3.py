class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def putdata(self):
        print(f"roll:{self.roll} name:{self.name}")

print("Main code block")
s1=Student(101,"VAIBHAVI")
s2=Student(102,"RUPALI")
s1.putdata()
s2.putdata()
