from flask_sqlalchemy import SQLAlchemy

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.secret_key = "QV02RLu8B2jcSJFIdxy5RtWcJ3CQFhJK"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

import blogform
import models
from flask.globals import session
from models import BlogModel

db.create_all()
