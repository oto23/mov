from movies import db
from sqlalchemy import desc

class MovieList(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    release = db.Column(db.Integer, unique=True, nullable=False)

    @staticmethod
    def mlist():
        return MovieList.query.order_by(desc(MovieList.id)).all()





















