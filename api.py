#!/usr/local/bin/python
# coding: utf-8

import requests
import json
import media


BASE_MOVIE_URL = 'http://api.themoviedb.org/3/movie/'
BASE_POSTER_URL = 'http://image.tmdb.org/t/p/w500'
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='


"""
Esse método retorna da API o primeiro trailer encontrado para o filme (id)
especificado.
"""


def getTrailerFromApi(movieId, api_key):
    url = BASE_MOVIE_URL + str(movieId) + '/videos?api_key='
    response = requests.get(url + api_key)

    if response.status_code != 200:
        return ''

    trailers_json = json.loads(response.content)['results']
    if len(trailers_json) > 0:
        return BASE_YOUTUBE_URL + trailers_json[0]['key']
    else:
        return ''


"""
Esse método retorna da API uma lista de filmes (objetos media.Movie) de acordo
com a ordenação selecionada.
"""


def getMoviesFromApi(sort_order):
    with open('api_key.txt') as file:
        API_KEY = file.readline()

    url = BASE_MOVIE_URL + sort_order + '?api_key='
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
                                  getTrailerFromApi(movie['id'], API_KEY)))

    return movies
