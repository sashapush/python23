MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
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
        print_movie(movie)
def print_movie(movie):
    print(f"Title {movie['title']}; Director - {movie['director']}; Year - {movie['year']}")


def find_movie():
    #first class function activated
    movie_title = input("Input movie title")
    for movie in movies:
        if movie["title"] == movie_title:
            print_movie(movie)
# Create other functions for:
#   - listing movies
#   - finding movies


user_options = { #dictionary with functions
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}
# And another function here for the user menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
menu()
