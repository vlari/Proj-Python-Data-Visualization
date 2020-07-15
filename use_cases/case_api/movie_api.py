import json
import requests


def load_movie_genres():
    """Load movie genres"""
    genres_file = 'genres.json'
    with open(genres_file) as file:
        data = json.load(file)

    return data['genre_options']


def get_selection():
    genres = load_movie_genres()
    print('Please choose a movie genre')
    for key, value in genres.items():
        print(f'{key}--{value}\n')

    index = input('Select Movie Genre')
    movie_genre = 'Invalid Genre'
    for key, value in genres.items():
        if index == key:
            movie_genre = value

    return movie_genre


def main():
    selected_genre = get_selection()
    source_url = f'https://yts.mx/api/v2/list_movies.json'
    response = requests.get(source_url,
                            params={'genre': f'{selected_genre}', 'limit': '20'},
                            headers={'Accept': 'application/json'}
                            )
    movies_response = response.json()
    print(f'********{selected_genre} Movies********')
    for movie in movies_response['data']['movies']:
        print('**********************')
        title = movie['title']
        description = movie['summary']
        year = movie['year']
        rating = movie['rating']

        print(f'Title: {title}\nDescription: {description}\nYear: {year}\nIMDB Rating: {rating}')
        print('**********************')


if __name__ == '__main__':
    main()
