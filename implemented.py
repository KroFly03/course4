from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
#from dao.user_movies import UserMoviesDAO
from database import db
from services.auth import AuthService
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from services.user import UserService
#from services.user_movies import UserMoviesService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)

#user_movies_dao = UserMoviesDAO(db.session)
#user_movies_service = UserMoviesService(user_movies_dao)
