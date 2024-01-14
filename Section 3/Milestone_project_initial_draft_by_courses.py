MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
def list_movies():
    for movie in movies:
        print(f"Title {movie['title']}; Director - {movie['director']}; Year - {movie['year']}")
def find_movies():
    movie_title = input("Input movie title")
# Create other functions for:
#   - listing movies
#   - finding movies

# And another function here for the user menu
def menu():
    operations = {"a": add_movie(), "l": list_movies, "f": find_movies}
    selection = input(MENU_PROMPT)
    while selection != 'q':
        operation = operations[selection]
        print(operation)
        # else:
        #     print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
menu()
