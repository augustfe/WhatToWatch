import pandas as pd
from imdb import Cinemagoer
from imdb.helpers import sortedEpisodes
from numpy import random
import os

ia = Cinemagoer()


def chooseSeries() -> tuple[str, str]:
    df = pd.read_csv("serier.csv", dtype={"title": "string", "ID": "string"})
    show = df.sample()
    title, id = show.values[0]
    return title, id


def chooseEpisode(id: str):
    series = ia.get_movie(id)
    print(".", end="", flush=True)
    ia.update(series, "episodes")
    print(".", end="", flush=True)
    episodes = sortedEpisodes(series)
    print(".", flush=True)
    n = len(episodes)
    i = random.randint(0, n)
    return episodes[i]


if __name__ == "__main__":
    title, id = chooseSeries()
    os.system("clear")
    print("Looking for something to watch", end="", flush=True)
    episode = chooseEpisode(id)
    print(
        f"""How about watching {title},
S: {episode["season"]} E: {episode["episode"]}, {episode["title"]}?
It has a rating of {episode["rating"]}."""
    )
