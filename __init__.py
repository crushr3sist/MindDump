from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "QV02RLu8B2jcSJFIdxy5RtWcJ3CQFhJK"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from flask.globals import session

import blogform
import models
from models import BlogModel

db.create_all()
