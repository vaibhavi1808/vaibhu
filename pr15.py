a=[]
n=int(input("Enter a value of n :"))
for i in range(n):
 no=int(input("Enter a numbers :"))
 a.append(no)

 lar=0
for i in range(len(a)):
    j=i+1
for j in range(len(a)-1):
    mul=a[i]*a[j]
    if mul>lar:
         lar=mul

print("Maximum product of an array: ",lar)
