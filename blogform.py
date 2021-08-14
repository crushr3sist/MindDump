from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    
    UsersName = StringField('UsersName')
    blogTitle = StringField('blogTitle')
    blogBody  = TextAreaField('blogBody')    
    submit    = SubmitField('submit')

