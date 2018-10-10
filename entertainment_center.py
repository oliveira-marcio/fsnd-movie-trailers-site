#!/usr/local/bin/python
# coding: utf-8

import fresh_tomatoes
from api import getMoviesFromApi


def main():
    orders = ['popular', 'top_rated']
    valid_choices = ['p', 't']

    valid_selection = False
    while not valid_selection:
        user_selection = input('Escolha a ordenação dos filmes '
                               '(p - Populares, t - Top Rated): ')
        valid_selection = user_selection.lower() in valid_choices

    print('Carregando filmes...')
    selected_order = orders[valid_choices.index(user_selection)]
    movies = getMoviesFromApi(selected_order)
    if len(movies) > 0:
        print('Filmes prontos. Abrindo browser...')
        fresh_tomatoes.open_movies_page(movies)
    else:
        print('Não foi possível carregar os filmes. Tente mais tarde.')


main()
