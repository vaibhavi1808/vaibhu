class student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def putdata(self):
        print(f"roll={self.roll} name={self.name}")
print("Main block code")
s1=student(101,"vaibhavi")
s2=student(102,"Rupali")
s1.putdata()
s2.putdata()