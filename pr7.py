def vowel():
    word=input("Enter a word=")
    cnt1=0
    for i in range(len(word)):
        if(word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u'):
            cnt1=cnt1+1
    print("Total vowel are=",cnt1) 
vowel()           