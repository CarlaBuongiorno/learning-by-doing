'''
    dojo_movie_database.py : This program will import the movie data, and then provide a menu of options to the user. 
    The user can select an option, the program will do it, and afterwards the program should return to the main menu. 
    
    The options are:

    List : List the name and year of all movies, separated by a comma.
    Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
    Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
    Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. 
          This new movie should show up in the other searches.
    Quit : Ends the program.
'''

import movie_data


def main():
    movie_list = movie_data.movies
    main_menu = True
    while main_menu:
        menu_option = menu_options()
        navigate(menu_option, movie_list, main_menu)
        input('\nPress enter to return to the main menu ')


def menu_options():
    option = int(input('\nWhat would you like to do?\
           \n\
           \nOption 1: Display all Movies\
           \nOption 2: Search Movies by Actor\
           \nOption 3: Search Movies by Genre\
           \nOption 4: Add Movie\
           \nOption 5: Quit\n\n'))
    return option


# Borrowed from Gijs ter Haar
def navigate(menu_option, movie_list, main_menu):
    menu_list = [display_all_movies, search_movies_by_actor, search_movies_by_genre, add_movie_to_db, quit]
    return menu_list[menu_option -1](movie_list, main_menu)


def display_all_movies(movie_list, main_menu):
    for movie in movie_list:
        title = movie['title']
        year = movie['year']
        print(f'{title}, {year}')
    return main_menu


def search_movies_by_actor(movie_list, main_menu):
    requested_actor = input("Which Actor's Movies would you like to see? ")
    movies_starring_actor = {}
    for movie in movie_list:
        for actor in movie['actors']:
            if requested_actor.title() in actor:
                if actor in movies_starring_actor:
                    movies_starring_actor[actor].append({movie['title']: movie['year']})
                else:
                    movies_starring_actor[actor] = [{movie['title']: movie['year']}]
    return print_movies_starring_actor(movies_starring_actor, main_menu, requested_actor, movie_list)


def print_movies_starring_actor(movies_starring_actor, main_menu, requested_actor, movie_list):
    if movies_starring_actor:
        for actor, movie in movies_starring_actor.items():
            print(f'\n{actor} starred in:')
            for movie_dict in movie:
                for title, year in movie_dict.items():
                    print(f'{title} in the year {year}') 
        return main_menu
    print(f'Sorry, we have no movies starring "{requested_actor}" in our database.')
    return search_movies_by_actor(movie_list, main_menu)
        

def search_movies_by_genre(movie_list, main_menu):
    genre = input('Which genre would you like to see? \n\n')
    print()
    genre_list = []
    for movie in movie_list:
        if genre.lower() in movie['genre']:
            genre_list.append(movie)
    if genre_list:
        for movie in genre_list:
            print(movie['title'], movie['year'])
    else:
        print(f'Sorry, we have no "{genre}" movies in our database.')
        search_movies_by_genre(movie_list, main_menu)
    return main_menu


def add_movie_to_db(movie_list, main_menu):
    new_movie = {}
    title = input('Title: ').capitalize()
    actors = input('Actors (full names separated by a comma): ').title().split(', ')
    year = int(input('Year: '))
    genre = input('Genre: ')
    rating = int(input('Rating: '))
    return add_new_movie(movie_list, main_menu, new_movie, title,actors, year, genre, rating)


def add_new_movie(movie_list, main_menu, new_movie, title,actors, year, genre, rating):
    new_movie['title'] = title
    new_movie['actors'] = actors
    new_movie['year'] = year
    new_movie['genre'] = genre
    new_movie['rating'] = rating
    movie_list.append(new_movie)
    return movie_list, main_menu


def quit(movie_list, main_menu):
    exit()


if __name__ == '__main__':
    main()


'''

def navigate(menu_option, movie_list, main_menu):
    if menu_option == '1':
        display_all_movies(movie_list)
        input('\nPress enter to return to the main menu ')
        return main_menu
    elif menu_option == '2':
        search_movies_by_actor(movie_list)
        input('\nPress enter to return to the main menu ')
        return main_menu
    elif menu_option == '3':
        search_movies_by_genre(movie_list)
        input('\nPress enter to return to the main menu ')
        return main_menu
    elif menu_option == '4':
        add_movie_to_db(movie_list)
        return 4
    else:
        exit()

The nicer way is to not print anything inside the loops at all. 
Make a new list outside the loop called movies_starring_actor or something, 
and add the movies (or just the titles and years) to that list as you go through the loops. 
Then, at the end, after the loops, You can print the contents. 
The nice thing about this is that you're keeping your processing and your output separate. 
It also means that you know if any movies were found, 
so you can print something like "Sorry, but 'Sander Hilgena' is not in any movies."

'''