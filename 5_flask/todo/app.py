from flask import Flask, g
from flask import render_template
import os
import sqlite3

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secretKey',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='My tasks'
))

def get_db():
    if not g.get('gb'): # when ther is no global connection, should create it
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con
    return g.db

@app.teardown_appcontext
def close_db(error):
    if g.get('db'):
        g.db.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    db = get_db()
    tasks = db.execute('SELECT * FROM tasks ORDER BY added_at DESC;').fetchall()
    return render_template('task_list.html', tasks=tasks)


if (__name__ == '__main__'):
    app.run(debug=True)