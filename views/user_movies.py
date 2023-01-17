from flask_restx import Resource, Namespace
from dao.models.user_movies import UserMoviesSchema
from flask import request
from implemented import user_movies_service
from decorators import auth_required


favourites_ns = Namespace('favourites')

user_movies_schema = UserMoviesSchema()
users_movies_schema = UserMoviesSchema(many=True)


@favourites_ns.route('/movies/<int:movie_id>')
class FavouritesView(Resource):
    #@auth_required
    def post(self, movie_id):
        data = request.json
        data['movie_id'] = movie_id
        return user_movies_service.add_favourite_movie(data)

    #@auth_required
    def delete(self, movie_id):
        data = request.json
        data['movie_id'] = movie_id
        return user_movies_service.add_favourite_movie(data)
