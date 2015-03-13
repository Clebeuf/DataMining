from io import StringIO
from StringIO import StringIO
import sys
import re
import string
import json
import requests
from rottentomatoes import RT
import time

#----------------------------------------------------------------------------------------------
# gets reviews from all critiques
#----------------------------------------------------------------------------------------------
def getAllReviews(api_key, movie_id):

    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

    #these are the "get parameters"
    #http://developer.rottentomatoes.com/docs/read/json/v10/Movie_Reviews
    options = {'review_type': 'all','page_limit': 50, 'page': 1, 'apikey': api_key}
    
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    reviews = data['reviews']

    for record in reviews:
        record["movieID"] = movie_id
        print json.dumps(record, indent=2)

    options = {'review_type': 'all','page_limit': 50, 'page': 50, 'apikey': api_key}
    
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    reviews = data['reviews']

    for record in reviews:
        record["movieID"] = movie_id
        print json.dumps(record, indent=2)






#----------------------------------------------------------------------------------------------
# get reviews
#----------------------------------------------------------------------------------------------
def getReviews(api_key, movieIDs):

    for movie_id in movieIDs:
        getAllReviews(api_key, movie_id)

#----------------------------------------------------------------------------------------------
# create movie array
#----------------------------------------------------------------------------------------------
def createMovieArray(movies):

    movieIDs = []

    for x in movies:
        movies = re.split('\r',x)

    for movie in movies:
        record = re.split('\t',movie)
        movieID = record[2]

        if len(movieID) == 5:
            movieID = '00' + movieID
        elif len(movieID) == 6:
            movieID = '0' + movieID

        movieIDs.append(movieID)


    return movieIDs


#----------------------------------------------------------------------------------------------
# based on code from http://nbviewer.ipython.org/github/xbsd/content/blob/master/HW3_solutions.ipynb
#   Queries the RT movie_alias API. Returns the RT id associated with an IMDB ID,
#   or raises a KeyError if no match was found
# ----------------------------------------------------------------------------------------------
def rt_id_by_imdb(imdbIDs, api_key):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json'

    rtID = []

    for movieID in imdbIDs:

        # added timeout so that we dont exceed the max # calls per second
        time.sleep(.2)

        params = dict(id=movieID, type='imdb', apikey=api_key)
        r = requests.get(url, params=params).text
        r = json.loads(r)

        rtID.append(r['id'])

        f1=open('./imbd-rottenTomato.txt', 'a')
        temp = movieID + ',' + str(r['id']) + '\n'
        f1.write(temp)

        getAllReviews(api_key, r['id'])

    return rtID

#----------------------------------------------------------------------------------------------
# main
#----------------------------------------------------------------------------------------------
def main():
    api_key = sys.argv[1]
    lensData = open(sys.argv[2])

    movieIDs = createMovieArray(lensData)

    rt_id_by_imdb(movieIDs, api_key)

if __name__ == '__main__':
    main()