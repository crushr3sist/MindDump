from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key='QV02RLu8B2jcSJFIdxy5RtWcJ3CQFhJK'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

import models, blogform
from models import BlogModel
from flask.globals import session
db.create_all()

