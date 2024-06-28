from flask import render_template
from . import db
from .models import Restaurant
from flask import current_app as app

@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)
