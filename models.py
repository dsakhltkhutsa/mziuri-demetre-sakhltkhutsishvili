from ext import db

class Movie(db.Model):
    __tablename__ = "Movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_year = db.Colomn(db.Integer(), nullable=False)
    image = db.Column(db.String(), default="default_image.jpg")
