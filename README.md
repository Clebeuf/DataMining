# Course Project for Data Mining
### SENG 474 & CSC 578D

**Overview:**
* For the scope of this project we will be trying to predict the freshness rating for a movie, based on the user reviews.  In order to enhance our predictions, we will be analyzing the sentiment of Rotten Tomatoe Reviews.

**Data Sources:**
* A Subset of the Movie Lens Data: https://raw.github.com/cs109/cs109_data/master/movies.dat
  * Contains approximately 9,400 movies (titles & IMDB ID)
  * Adapted from: http://grouplens.org/datasets/movielens/
* Rotten Tomatoes API: http://developer.rottentomatoes.com/
 * Reviews API: http://developer.rottentomatoes.com/docs/read/json/v10/Movie_Reviews
 * Movie Alias API: http://developer.rottentomatoes.com/docs/read/json/v10/Movie_Alias 

**Additional Options:**
* Get the abridged cast list
 * http://developer.rottentomatoes.com/docs/read/json/v10/Movie_Info
* Preprocess the comments a bit more
 * removing stopwords
 * stemming (Porter or KSTEM)
 * convert everything into the same case
 * remove "junk"
 * sentiment analysis: http://www.nltk.org/api/nltk.html

The Tomatometer: http://www.rottentomatoes.com/about/     
Related Kaggle: https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews    
Movie Lens Dataset: http://grouplens.org/datasets/movielens/

**Related Work:**
* http://datapsych.weebly.com/blog/bayesian-tomatoes-using-machine-learning-and-text-analysis-to-predict-reviewer-sentiment
* http://nbviewer.ipython.org/github/xbsd/content/blob/master/HW3_solutions.ipynb
* http://www.farsiteforecast.com/rotten-tomatoes/
* http://www.slate.com/articles/arts/culturebox/2011/06/slates_hollywood_careeromatic.html
* http://www.vulture.com/2013/07/summer-movie-quiz-guess-the-rotten-tomato-score.html

