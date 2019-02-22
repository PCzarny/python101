import os
from flask import Flask, g
from peewee import SqliteDatabase

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secretKey',
    TITLE='Quiz ORM Peewee',
    DATABASE=os.path.join(app.root_path, 'quiz.db')
))

base = SqliteDatabase(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = base
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response