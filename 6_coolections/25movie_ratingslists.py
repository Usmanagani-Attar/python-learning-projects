a=int(input("Enter 1 if you want to give custom moveis or else enter 2 : "))

movies = ["War","Dabang","Kantara","Pushpa","SpiderMan","KGF"]
ratings =[]

if a==1:

    movies1=[]
    n=int(input("Enter the number of movies that you want to give : "))
    for i in range(1,n+1):
        movies1.append(input(f"Enter the Number {i} movie name : "))
    print("Let's rate the movies")
    print()
    for m in movies1:
        ratings.append(input(f"give the Ratings for {m} (1-5) : "))
    maxrate=max(ratings)
    maxindex=ratings.index(maxrate)
    maxratedmovie=movies1[maxindex]
    print()
    print(f"Your maximum rating is {maxrate} ⭐ That is to the movie {maxratedmovie}")

elif a==2:
    print("Let's rate the movies")
    print()    
    for m in movies:
        ratings.append(input(f"give the Ratings for {m} (1-5) : "))
    maxrate=max(ratings)
    maxindex=ratings.index(maxrate)
    maxratedmovie=movies[maxindex]
    print()
    print(f"Your maximum rating is {maxrate} ⭐ That is to the movie {maxratedmovie}")
else:
    print("Please Enter the valid choice(1-2)")