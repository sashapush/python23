#higher order functions are the ones which accept other functions as parameters

def greet():
    print("Hello")

hello = greet

def before_and_after(func):
    print("Before...")
    func() #runs a function, if we pass not a function - we'll get an error
    print("After..")

#before_and_after(lambda :5) #ok, since lambda is a function
#before_and_after(greet) #pass the function by name, not ()
#before_and_after(hello) #same as above

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
    {"name": "Ass is", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]
def find_movie(expected,finder):
    found = [] #so that >1 result can be returned
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found

#find a movie from the list of dictionaries above:
find_by = input("What property are you searching by?")
looking_for = input("What are you looking for?")
#find_movie(lambda movie: movie[find_by]) - while find_movie had only "finder" function - we get all moviews
movies = find_movie(looking_for, lambda movie: movie[find_by]) #lambda function takes in an argument and
# returns find_by property of movie argument, assuming that movie is a dictionary

print(movies or "No movies found.") #if there are no movies
#Result:
# What property are you searching by?name
# What are you looking for?The Matrix
# {'name': 'The Matrix', 'director': 'Wachowski'}

