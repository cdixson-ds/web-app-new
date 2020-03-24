# Create some database models
from app import db


class User(db.Model):

    __tablename__ = "users" # Name of the database table

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    occupation = db.Column(db.String(255), nullable=False)

    # Other input fields

