movies=[]

def add_movie():
    Movie_id=int(input("Enter movie id="))
    Title=input("Enter title=")
    Director=input("Enter director=")
    Genre=input("Enter genre=")
    Year_released=int(input("Enter year released="))
    Rating=float(input("Enter rating="))

    movies.append('movieid':Movie_id,'title':Title,'director':Director,'genre':Genre,'year released':Year_released,'rating':Rating)
    print("Movie added successfully")

def view_movies():
    if(len(movies)==0):
        print("No movies in the collection")
    else:
        print("movieid \t title \t director \t genre \t year released \t year released \t rating")
        for i in (len(movies)):
            print(Movie_id[i])




            

def calculate_average_rating():
    if(len(movies)==0):
        print("No movies in collection")
    else:
        total_rating=0
        for i in (len(movies)):
            total_rating+=i[Rating]
            average_rating=int(average_rating*100)/100
        print("average rating for all movies=",average_rating)    




        


count=3
while(count!=0):
        uname=input("enter the user name=")
        upass=input("enter the user password=")
        if(uname=="admin" and upass=="1234"):
            print("login successfully")
            print("*****Movie collection management syatem****")
            cnt=1
            while(cnt!=0):
                print("1.Add movie \n 2.view movies \n 3.calculate average rating \n 4.exit")
                ch=int(input("Enter your choice="))
                if ch==1:
                    print("Add movies")
                    add_movie()
                elif ch==2:
                    print("view movies")
                    view_movies()
                elif ch==3:
                    print("Calculate average rating")
                    calculate_average_rating()
                elif ch==4:
                    cnt=0
                else:
                    print("invalid choice...please try again.")     
                count=1
                if(uname!="admin" and upass!="1234"):
                    print("Login unsuccessfully both are incorrect")
                if(uname!="admin"):
                    print("incorrect user name")
                if(upass!="1234"):
                    print("Incorrect user password")
count-=1
print("remaining attempts=",count)
                

              
        