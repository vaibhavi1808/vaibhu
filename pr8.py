def palindrome():
    revs=""
    str=input("Enter a string=")
    for i in str:
        revs=i+revs
    print("The reversed string is=",revs) 
palindrome()       