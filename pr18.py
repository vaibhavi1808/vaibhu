def first_repeat(str):
    for i in range(len(str)):
        cnt=str.count(str[i])
        if cnt==1:
            re=str[i]
            break
    return re

str=input("Enter a string=")
nch=first_repeat(str) 
print("The character is non repeating=",nch)   