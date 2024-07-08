#str2=[]

def palindrome():
    revs=""
    str1=input("Enter a string=")
    for i in str1:
        revs=i+revs
    print(revs) 
    if(str1==revs):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

palindrome()          