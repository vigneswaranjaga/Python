
""" This is a movie collection system
    1. Add movies to the database
    2. View movies that is stored
    3. Find the movies based on (Director name or year)
"""
# All the movies is been stored in a dictionary

print("******* This is a movie Collection System ********")

all_Movies = {

        '1':{
     'name': 'The Matrix',
     'director': 'Wachowskis',
     'year': '1994'
    },

       '2':{
     'name': 'The Matrix Revolution 2',
     'director': 'Wachowskis',
     'year': '1996'
    },
       '3': {
     'name': 'The Avengers',
     'director': 'Marvel',
     'year': '2012'
    },
      '4': {
     'name': 'The Avengers End game',
     'director': 'Marvel',
     'year': '2018'
    },
    '5':   {
     'name': 'The Thor',
     'director': 'Stanlee',
     'year': '2011'
    },
       '6': {
     'name': 'Spider Man',
     'director': 'MarvelMan',
     'year': '2012'
    },
        '7':{
     'name': 'The Matrix 3',
     'director': 'Wacho',
     'year': '1994'
    },
        '8':{
     'name': 'The Salt',
     'director': 'Lee',
     'year': '1996'
    },
       '9': {
     'name': 'Last Game',
     'director': 'X',
     'year': '2018'
    },
       '10': {
     'name': 'Iron Man',
     'director': 'Marvel Studios',
     'year': '2015'
    }
        
}


print("Select the Options: \n 1. Add Movies to the Collection \n 2. View the list of movies in the collection \n 3. Find the Movies \n 4. EXIT")
option_selected = int(input("Enter the option: "))
   
def view_movies():
    print("Which you want to be listed: \n 1. Film Name and Year \n 2. Film name and Director Name \n 3. All the details")
    option_View_Movies = int(input("Enter the options to be listed: "))

    if(option_View_Movies ==1):
        for film in all_Movies:
            print(f"The movie names are {film['name'],film['year']}")

    elif(option_View_Movies ==2):
        for film in all_Movies:
            print(f"The director names are {film['director'],film['name']}")
    elif(option_View_Movies ==3):
        for film in all_Movies:
            print(f"The film details are {film['director'],film['name'],film['year']}")

    else:
        wish = input("Do you wish to sort movies [Y]/[N]: ")
        if(wish == 'y'):
            find_Movies()
        else:
            Option()    


def find_Movies():
    print("Which option would you like to select to filter : \n 1. Film Year \n 2. Director Name ")
    option_Find_Movies = int(input("Enter the options to be listed: "))

    if(option_Find_Movies ==1):
        movie_year =input("Enter the year to filter movies")
        for film in all_Movies['year']:
            if (film == '2018'):
                print(f"The movie names are {film['name'],film['director']}")

    if(option_Find_Movies ==2):
        for film in all_Movies:
            print(f"The movie names are {film['name'],film['year']}")

    else:
        print("Please select the correct option ")


def Add_Movies():
     print(" Adding Movies to the database")
     for k in all_Movies.keys():
         all_Movies[k] = input (f"Enter the movie {k}")






if(option_selected == 1):
    print("You have selected an option to add a movie to the collection")

    Add_Movies()

elif (option_selected == 2):
    print("You have selected an option to view all the movies in the collection")

    view_movies()

elif (option_selected == 3):
    print("You have selected an option to Find the movies in the collection")

    find_Movies()

elif (option_selected == 4):
    print("You have selected an option to Exit from Movie Collection")
    
else:
    print("Please select the correct option ")
 






    






