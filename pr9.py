def frequency():
    word=input("Enter a word=")
    cnt=0
    for i in word:
        cnt=word.count(i)
        print("character",i,"repeated",cnt,"times")
frequency()    