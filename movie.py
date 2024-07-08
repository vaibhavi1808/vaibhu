movie_id = []
title = []
director = []
genre = []
year = []
rating = []

def add_movie():
    nmovie_id = int(input("Enter Movie ID: "))
    ntitle = input("Enter Title: ")
    ndirector = input("Enter Director: ")
    ngenre = input("Enter Genre: ")
    nyear = int(input("Enter Year Released: "))
    nrating = float(input("Enter Rating: "))
    
    movie_id.append(nmovie_id)
    title.append(ntitle)
    director.append(ndirector)
    genre.append(ngenre)
    year.append(nyear)
    rating.append(nrating)
    print("Movie added successfully.")

def view_movies():
    print("movie_id \t title \t director \t genre \t year \t rating")
    for i in range(len(movie_id)):
        print(movie_id[i],"\t",title[i],"\t",director[i],"\t",genre[i],"\t",year[i],"\t",rating[i])


def update_info():
     fmovie_id=input(" enter the find movie id")
     for i in range(len(movie_id)):
          if(movie_id[i]==fmovie_id):
            umovie_id=input("enter movie id=")
            utitle=input("enter movie title=")
            udirector=input("enter movie director=")
            ugenre=input("Enter the movie genre=")
            uyear=input("Enter the movie released year=")
            urating=input("Enter the movie rating=")

            movie_id[i]=umovie_id
            title[i]=utitle
            director[i]=udirector
            genre[i]=ugenre
            year[i]=uyear
            rating[i]=urating 

def deletedata():
     dmovie_id=input("enter the movie id of delete")
     for i in range(len(movie_id)):
          if(movie_id[i]==dmovie_id):
               movie_id.remove(movie_id[i])
               title.remove(title[i])
               director.remove(director[i])
               genre.remove(genre[i])
               year.remove(year[i])
               rating.remove(rating[i])
               break
          
def calculate_average_rating():
    if len(rating) == 0:
        print("No movies in the collection.")
    else:
        total_rating = sum(rating)
        average_rating = total_rating / len(rating)
        average_rating = int(average_rating * 100) / 100
        print("Average rating for all movies:", average_rating)


    
count=3
while(count!=0):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if(username == "admin" and password == "1234"):
        print("Login Successfully")
        cnt=1
        while(cnt!=0):
            print("Movie Collection Management System")
            print("1. Add Movie\n2. View Movies\n3. Calculate Average Rating\n4. update \n 5.delete \n 6.exit")
            ch=int(input("Enter Your Choice = "))
            if ch==1:
                print("Add Movies")
                add_movie()
            elif ch==2:
                print("View Movies")
                view_movies()
            elif ch==3:
                print("Update data")
                update_info()
            elif ch==4:
                print("Delete data")    
                deletedata()
            elif ch==5:
                print("Calculate Average Rating")
                calculate_average_rating()
            elif ch==6:
                print("Exit")
                cnt=0    

            
        count=1
    if(username!="admin" and password!="1234"):
        print("Authentication Invalide Both are Incorrect")
    if(username!="admin"):
        print("Please enter Correct Username")
    if(password!="1234"):
        print("Please enter Correct Password")
    count-=1
    print("Remaining Attempts = ",count)