from . import db

class Restaurant(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Float)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
