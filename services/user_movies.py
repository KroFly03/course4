from dao.user_movies import UserMoviesDAO
from dao.models.user_movies import UserMovies


class MovieService:
    def __init__(self, dao: UserMoviesDAO):
        self.dao = dao

    def add_favourite_movie(self, data):
        if None in data:
            raise Exception

        user_movie = UserMovies(**data)

        return self.dao.add_favourite_movie(user_movie)

    def delete_favourite_genre(self, data):
        if None in data:
            raise Exception

        user_movie = UserMovies(**data)

        return self.dao.delete_favourite_genre(user_movie)
