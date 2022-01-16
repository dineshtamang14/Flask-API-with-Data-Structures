from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from flask import Flask, request, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

# appp
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.db"
app.config["SQL_TRACK_MODIFICATIONS"] = 0


# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer)

