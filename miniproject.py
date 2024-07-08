Roll_no=[]
Name=[]
Marks=[]

def addstud():
        sroll=input("enter student roll number=")
        sname=input("enter the student name=")
        smarks=input("enter student marks=")
        
        Roll_no.append(sroll)
        Name.append(sname)
        Marks.append(smarks)

def viewlist():
        print("Roll_no \t Name \t Marks")
        for i in range(len(Roll_no)):
           print(Roll_no[i]," \t",Name[i]," \t",Marks[i])

def updatedata():
     froll=input(" enter the find roll")
     for i in range(len(Roll_no)):
          if(Roll_no[i]==froll):
            uroll=input("enter student roll no=")
            uname=input("enter student name=")
            umarks=input("enter student marks=")

            Roll_no[i]=uroll
            Name[i]=uname
            Marks[i]=umarks    

def deletedata():
     droll=input("enter the roll number of delete")
     for i in range(len(Roll_no)):
          if(Roll_no[i]==droll):
               Roll_no.remove(Roll_no[i])
               Name.remove(Name[i])
               Marks.remove(Marks[i])
               break

count=3
while(count!=0):
    uname=input("enter the user name=")
    upass=input("enter the user password=")
    if(uname=="admin" and upass=="1234"):
         print("login successfully")
         print("*****student management system****")
         cnt=1
         while(cnt!=0):
            print("1.Add student \n 2.view list \n  3.Update \n 4.Delete  \n 5.Exit")
            ch=int(input("enter your choice"))
            if(ch==1):
                print("**Add student**")
                addstud()
            if(ch==2):
                print("**View list**")
                viewlist()
            if(ch==3):
                print("**Update**")
                updatedata()
            if(ch==4):
                print("**Delete**")
                deletedata()
            if(ch==5):
                print("**Exit**")  
                cnt=0  
         count=1        
    elif(uname!="admin" and upass!="1234"):
         print("login un-successfully both incorrect")
    elif(uname!="admin"):
         print("incorrect user name")
    elif(upass!="1234"):
         print("incorrect user password")
    
count-=1
print("remaining attempt=",count) 

   



    
     



    