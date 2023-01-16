from flask_restx import Resource, Namespace
from dao.models.user_movies import UserMoviesSchema
from decorators import auth_required


favourites_ns = Namespace('favourites')

user_movies_schema = UserMoviesSchema()
users_movies_schema = UserMoviesSchema(many=True)


@favourites_ns.route('/movies/<int:movie_id>')
class FavouritesView(Resource):
    #@auth_required
    def post(self, movie_id):
        pass

    #@auth_required
    def delete(self, movie_id):
        pass
