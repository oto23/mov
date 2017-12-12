import os
from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import MovieForm



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'movie.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'


db = SQLAlchemy(app)
import mlist
import models

Bootstrap(app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_movies=models.MovieList.mlist(), movdict=mlist.movdc)


@app.route('/add', methods=['Get', 'Post'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        name = form.name.data
        release = form.release.data
        mv = models.MovieList(name=name, release=release)
        db.session.add(mv)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
