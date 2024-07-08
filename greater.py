a=int(input("enter the value a"))
b=int(input("enter the value b"))
c=int(input("enter the value c"))
if(a>b and a>c):
    print("a is greater")

elif(b>a and b>c):
    print("b is greater")
elif(c>a and c>b):
    print("c is greater")
elif(a==b==c):
    print("all numbers are same")
elif(a==b and b!=c):
    print("a and b are aeual")
else:
    print(" b is not equal to c")