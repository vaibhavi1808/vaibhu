a=[]
n=int(input("Enter a value of n="))
for i in range(n):
    no=int(input("Enter a numbers="))
    a.append(no)
print(a)    
kst=int(input("enter a steps to rotate="))
for i in range(len(a)):
        if i<kst:
              a.append(a[0])
              a.pop(0)
              i=0
              if i>kst:
                    break
print(a)              
