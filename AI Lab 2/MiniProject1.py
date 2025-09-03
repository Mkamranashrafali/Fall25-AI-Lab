movies = [
("Eternal Sunshine of the Spotless Mind", 20000000),
("Memento", 9000000),
("Requiem for a Dream", 4500000),
("Pirates of the Caribbean: On Stranger Tides", 379000000),
("Avengers: Age of Ultron", 365000000),
("Avengers: Endgame", 356000000),
("Incredibles 2", 200000000)
]
user_movies=[]
def add_movie():
    name=input("Enter movie name: ")
    try:
        budget = int(input("Enter movie budget: "))
        user_movies.append((name,budget))
    except ValueError:
        print("Invalid input! Please enter a number.")
def average():
    data=user_movies if user_movies else movies
    avg=sum(i[1] for i in data)/len(data)
    print("The average cost of movies is: ",avg)
    total_movies=0
    for i in data:
        if i[1]>avg:
            total_movies+=1
            diff=i[1]-avg
            print(i[0])
            print(f"The budget is higher then average is {diff}")
    if total_movies > 0:
        print("These movies have high budget then average cost.")
        print(f"The count of movies have high budget then average is {total_movies}")
    else:
        print("No movie has higher budget than average")
   
print("Note: There are some dummy data to check programe.You can add your data.")
print("1: To add movies ")
print("2: To display basic info")
while True:
    option=int(input("Chose a option:"))
    if option==1:
        add_movie()
    elif option==2:
        average()
    elif option==3:
        break
    else:
        print("Invalid input!Try again.")