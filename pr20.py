a=[]
n=int(input("Enter a value of n="))
for i in range(n):
    no=int(input("Enter a numbers="))
    a.append(no)

a.sort()
j=1
for i in range(n-1):
    if a[i]!=j:
        print("Missing no is=",j)
        j=j+1
        break

j=j+1        