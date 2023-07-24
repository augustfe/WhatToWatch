from imdb import Cinemagoer
from IPython.display import clear_output
from csv import writer

ia = Cinemagoer()


def addToList(name: str) -> None:
    movies = ia.search_movie(name)
    correct = None
    print('Assert correct found [y/n]')
    for movie in movies:
        response = input(f"{movie['long imdb title']} [y/n]")
        if response == 'y':
            correct = movie
            break
        clear_output(wait=True)

    if correct is None:
        print("Series was not found")

    with open('serier.csv', 'a') as f_object:
        writer_object = writer(f_object)
        title = correct['title']
        ID = correct.getID()
        writer_object.writerow([title, ID])

        f_object.close()
    
