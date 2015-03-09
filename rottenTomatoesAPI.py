from io import StringIO
from StringIO import StringIO
import sys
import re
import string
import json
import requests
from rottentomatoes import RT

#----------------------------------------------------------------------------------------------
# gets reviews from all critiques
#----------------------------------------------------------------------------------------------
def getAllReviews(api_key, movie_id):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

    #these are "get parameters"
    #options = {'review_type': 'all', 'page_limit': 20, 'page': 1, 'apikey': api_key}
    options = {'review_type': 'all','page_limit': 50, 'page': 1, 'apikey': api_key}
    
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    for record in data['reviews']:
        print json.dumps(record, indent=2)


#----------------------------------------------------------------------------------------------
# gets reviews from top crtitiques
#----------------------------------------------------------------------------------------------
def getTopCriticReviews(api_key, movie_id):
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/%s/reviews.json' % movie_id

    #these are "get parameters"
    options = {'review_type': 'top_critic', 'page_limit': 20, 'page': 1, 'apikey': api_key}
    data = requests.get(url, params=options).text
    data = json.loads(data)  # load a json string into a collection of lists and dicts

    for record in data['reviews']:
        print json.dumps(record, indent=2)


#----------------------------------------------------------------------------------------------
# main
#----------------------------------------------------------------------------------------------
def main():
    # APIKey = open(sys.argv[1])
    api_key = sys.argv[1]

    movie_id = '770672122'  # toy story 3

    # getTopCriticReviews(api_key)
    getAllReviews(api_key, movie_id)

if __name__ == '__main__':
    main()