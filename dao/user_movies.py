from dao.models.user_movies import UserMovies


class UserMoviesDAO:
    def __init__(self, session):
        self.session = session

    def add_favourite_movie(self, user_movie):
        self.session.add(user_movie)
        self.session.commit()

        return user_movie

    def delete_favourite_genre(self, user_movie):
        self.session.delete(user_movie)
        self.session.commit()

        return user_movie
