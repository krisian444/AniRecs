# Randomly recommends anime based on how what you're in the mood for today
# Uses Jikan API with JikanPy wrapper
# WIP

from random import choice, randint
import numpy as np
from jikanpy import Jikan
import time
from math import floor

#init Jikan instance
jikan = Jikan() # note this is limited to 2 requests / second

# let user select which mood they are feeling from based on selecting anime genre
def selectMood(Genre):
    print("What type of anime are you feeling today? Something...")

    for i, element in enumerate(Genre):
        print("{}) {}".format(i + 1, element))
        time.sleep(0.1)

    while(1):

        num = input("\nEnter selection: ")

        if 0 < int(num) <= len(Genre):
            return int(num) - 1
            break
        else:
            print("\nNot a valid selection, please try again \n")
            time.sleep(1)


# define major MAL genres and their IDs
genres = dict([(1, 'Action'), (2, 'Adventure'), (4, 'Comedy'), (8, 'Drama'), 
(10, 'Fantasy'), (14, 'Horror'), (7, 'Mystery'), (22, 'Romance'),
(24, 'Sci-fi'), (36, 'Slice of life'), (30, 'Sports'), (37, 'Supernatural')])

# get index of selected genre
gSelect = selectMood(list(genres.values()))

# get ID of selected genre
gChose = (list(genres))[gSelect]

#print("\n", gChose, "\n")

# this request defaults to the first page of MAL result
# each page only shows 100 anime at a time, have to generate
# again to randomly select a page
# there is probably a better solution to this, but for the time being I just want any recommendation

jikanRequest = jikan.genre(type = 'anime', genre_id = gChose)
time.sleep(1) # ensure I don't abuse the rate limit 

totalAnime = jikanRequest['item_count']
randPage = randint(0, floor(int(totalAnime)/100))

time.sleep (1) # to ensure I don't abuse the API rate limit
jikanRequest2 = jikan.genre(type = 'anime', genre_id = gChose, page = randPage)

# get dictionary of anime from selected mood/genre and get how many
aniList = jikanRequest2['anime']
itemCount = len(aniList)

randNum = randint(0, itemCount)

print("\nYou should watch:", aniList[randNum]['title'], '\n')