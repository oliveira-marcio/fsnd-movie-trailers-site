import requests
import json
import media
import fresh_tomatoes


BASE_MOVIE_URL = 'http://api.themoviedb.org/3/movie/'
BASE_POSTER_URL = 'http://image.tmdb.org/t/p/w500'
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
    
def getTrailerFromApi(movieId):
    with open('api_key.txt') as file:
        API_KEY = file.readline()

    url = BASE_MOVIE_URL + str(movieId) + '/videos?api_key='
    response = requests.get(url + API_KEY)
    
    if response.status_code != 200:
        return ''

    trailers_json = json.loads(response.content)['results']
    if len(trailers_json) > 0:
        return BASE_YOUTUBE_URL + trailers_json[0]['key']
    else:
        return ''
    

def getMoviesFromApi():
    with open('api_key.txt') as file:
        API_KEY = file.readline()

    url = BASE_MOVIE_URL + 'popular?api_key='
    response = requests.get(url + API_KEY)

    if response.status_code != 200:
        return []

    movies_json = json.loads(response.content)['results']
    if len(movies_json) == 0:
        return []

    movies = []
    for movie in movies_json:
        movies.append(media.Movie(movie['title'],
                                  movie['overview'],
                                  BASE_POSTER_URL + movie['poster_path'],
                                  getTrailerFromApi(movie['id'])))

    return movies
        
 
fresh_tomatoes.open_movies_page(getMoviesFromApi())
