from marshmallow import Schema, fields

from database import db


class UserMovies(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("user")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    movie = db.relationship("movie")


class UserMoviesSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
