def anagram(str1,str2):
    str1=sorted(str1)
    str2=sorted(str2)
    if str1==str2:
        return True
    else:
        return False

str1=input("Enter a string 1=")
str2=input("Enter a string 2=")
if anagram(str1,str2):
    print("Strings are angram ")
else:
    print("Strings are not angram")