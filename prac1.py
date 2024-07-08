def addition(a):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    return(sum) 

a=[]
print("main function")
n=int(input("Enter a size of array="))
for i in range(n):
        aa=int(input("Enter a numbers="))
        a.append(aa)
sum=addition(a)
print("The sum of all elements=",sum)         
