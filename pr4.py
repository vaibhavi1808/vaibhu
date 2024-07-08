a=[]
for i in range(5):
    aa=int(input("Enter elements="))
    a.append(aa)
print(a)
for i in range(len(a)):
    cnt=a.count(a[i])
    if cnt>1:
        a.pop(i)
        break
print(a)    