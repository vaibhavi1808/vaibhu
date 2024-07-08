a=[]
n=int(input("Enter size of the list="))
for i in range(n):
    aa=int(input("Enter the elements="))
    a.append(aa)
print(a)
for i in range(len(a)):
    if a[i]==0:
        a.append(a[i])
        a.pop(i)
print(a)             
