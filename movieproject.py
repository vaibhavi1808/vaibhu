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