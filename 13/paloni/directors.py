from collections import defaultdict, namedtuple, Counter
import csv


MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

Director = namedtuple('Director', 'name avg movies')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''

    directors = defaultdict(list)

    with open(MOVIE_DATA, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director_name = line['director_name']
                movie_title = line['movie_title']
                title_year = line['title_year']
                imdb_score = line['imdb_score']
                directors[director_name].append(
                    Movie(movie_title, title_year, imdb_score))
            except ValueError:
                pass
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    new_directors = []
    for director, movies in directors.items():
        if len(movies) >= 4:
            avg_score = round(_calc_mean(movies), 1)
            new_directors.append(
                Director(director, avg_score, movies))
    return sorted(new_directors, key=lambda director: director[1], reverse=True)


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total = 0
    for movie in movies:
        total += float(movie.score)

    return total / len(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''

    sep_line = '-' * 60

    for counter, item in enumerate(directors[:NUM_TOP_DIRECTORS]):
        print()
        print(f'{counter+1:02}. {item.name:<52} {item.avg}')
        print(sep_line)
        for movie in item.movies:
            print(f'[{movie.year}] {movie.title:<49} {movie.score}')


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
