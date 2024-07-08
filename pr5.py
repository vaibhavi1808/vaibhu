a=[]
b=[]
for i in range(5):
    aa=int(input("Enter element of an array 1="))
    a.append(aa)

for i in range(5):
    bb=int(input(" \n Enter the elements ofnarray 2="))
    b.append(bb) 

for i in range(5):
    for j in range(5):
        if a[i]==b[j]:
            cnt=a.count(i)
            if cnt<2:
             print("Intersections=",a[i])       