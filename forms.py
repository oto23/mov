from flask_wtf import FlaskForm
from wtforms.fields import StringField


class MovieForm(FlaskForm):
    name = StringField('Add a movie:')
    release = StringField('Add a date:')



