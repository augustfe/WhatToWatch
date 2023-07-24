from imdb import Cinemagoer
from csv import writer
import pandas as pd
import os

ia = Cinemagoer()


def addToList(name: str) -> None:
    movies = ia.search_movie(name)
    correct = None

    for movie in movies:
        os.system("clear")
        print("Assert correct found [y/n]")
        response = input(f"{movie['long imdb title']}\n")

        if response == "y":
            correct = movie
            break

    if correct is None:
        print("Series was not found")

    df = pd.read_csv("serier.csv", dtype={"title": "str", "ID": "str"})
    if correct.getID() in df.values:
        return

    with open("serier.csv", "a") as f_object:
        writer_object = writer(f_object)

        title = correct["title"]
        ID = correct.getID()
        writer_object.writerow([title, ID])

        f_object.close()
