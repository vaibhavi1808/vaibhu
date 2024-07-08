a=[]
b=[]
for i in range(5):
    aa=int(input("Enter the array 1 elements="))
    a.append(aa)
    a.sort()
print("first array=")
print(a)

for i in range(5):
    bb=int(input("Enter array 2 elements="))
    b.append(bb)
    b.sort()
print("second array=")
print(b)
a.extend(b)
print("Merged array=")
print(a)    