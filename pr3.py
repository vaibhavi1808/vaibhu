def second_large():
    n=int(input("enter a size of array="))
    for i in range(n):
        bb=int(input("enter the number="))
        b.append(bb)
    print(b)    


b=[]
second_large()
large=0
s_large=0
for i in range(len(b)):
    if(large<b[i]):
        s_large=large
        large=b[i]
    elif(s_large<b[i] and b[i]!=large):
        s_large=b[i]
print("The largest number is=",large) 
print("The second largest number is=",s_large)           


