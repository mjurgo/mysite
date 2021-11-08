import random

from flask import render_template

from mysite import app
from mysite.models import Poem


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/poem')
def poem():
    poem = random.sample(Poem.query.all(), 1)[0]
    print(poem)
    return render_template('poems/poem.html', poem=poem)
