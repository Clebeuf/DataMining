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
# Looks up movie reviews from RT id
#   - Input: TR id and api key
#   - Output: prints up to 100 reviews for the movie.
#----------------------------------------------------------------------------------------------
def getAllReviews(api_key, movie_id):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

    #these are the "get parameters" for the first 50 reviews (ie. pages 1-50)
    options = {'review_type': 'all','page_limit': 50, 'page': 1, 'apikey': api_key}
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    # print the reviews
    reviews = data['reviews']
    for record in reviews:
        record["movieID"] = movie_id
        print json.dumps(record, indent=2)

    #these are the "get parameters" for the second 50 reviews (ie. pages 50-100)
    options = {'review_type': 'all','page_limit': 50, 'page': 50, 'apikey': api_key}
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    # print the reviews
    reviews = data['reviews']
    for record in reviews:
        record["movieID"] = movie_id
        print json.dumps(record, indent=2)


#----------------------------------------------------------------------------------------------
# Create an array of IMBD movie ids from the file passes in
#----------------------------------------------------------------------------------------------
def createMovieArray(movies):

    # create an array to store the imbd ids
    movieIDs = []

    # get each of the lines in the input file
    for x in movies:
        movies = re.split('\r',x)

    # for each of the lines get the id
    for movie in movies:
        record = re.split('\t',movie)
        movieID = record[2]

        # since the ids range from 5-7 digits add 0s infront to make them all 7 digits
        if len(movieID) == 5:
            movieID = '00' + movieID
        elif len(movieID) == 6:
            movieID = '0' + movieID

        # add movie imbd id to the list
        movieIDs.append(movieID)

    # return the list of imbd ids
    return movieIDs


#----------------------------------------------------------------------------------------------
# Loosely based on code from http://nbviewer.ipython.org/github/xbsd/content/blob/master/HW3_solutions.ipynb
#   - Queries the RT movie_alias API. Returns the RT id associated with an IMDB ID
#   - When RT id is returned it prints it to imbd-rottenTomato.txt
#   - Makes a call to get reviews for the RT id
# ----------------------------------------------------------------------------------------------
def rt_id_by_imdb(imdbIDs, api_key):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json'

    # create new array to store ids
    rtID = []

    # for each of the IMBD ids look up RT id & get reviews
    for movieID in imdbIDs:

        # added a .2 second timeout so that we don't exceed the max 5 calls per second
        time.sleep(.2)

        # these are the "get parameters"
        # http://api.rottentomatoes.com/api/public/v1.0/movie_alias.json
        params = dict(id=movieID, type='imdb', apikey=api_key)
        r = requests.get(url, params=params).text
        r = json.loads(r)

        # add RT id to the array
        rtID.append(r['id'])

        # write imbd & RT id to logging file
        f1=open('./imbd-rottenTomato.txt', 'a')
        temp = movieID + ',' + str(r['id']) + '\n'
        f1.write(temp)

        # get reviews for the RT id
        getAllReviews(api_key, r['id'])

    return rtID

#----------------------------------------------------------------------------------------------
# main
#----------------------------------------------------------------------------------------------
def main():

    # pass in api key as argument 1
    api_key = sys.argv[1]

    #pass in file with IMDB id as argument 2 (ie. lens dataset)
    lensData = open(sys.argv[2])

    # creates a list of IMBD ids from the lens data
    movieIDs = createMovieArray(lensData)

    # looks up the rotten tomatoes id for each of the IMBD ids & prints reviews
    rt_id_by_imdb(movieIDs, api_key)

if __name__ == '__main__':
    main()