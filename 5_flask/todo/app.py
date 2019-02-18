from flask import Flask, g
from flask import render_template
import os
import sqlite3

from datetime import datetime
from flask import flash, redirect, url_for, request

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

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    error = None
    if request.method == 'POST':
        description = request.form['task'].strip()
        if len(description) > 0:
            db = get_db()
            db.execute('INSERT INTO tasks VALUES (?, ?, ?, ?);',
                        [None, description, '0', datetime.now()])
            db.commit()
            flash('New task added!')
            return redirect(url_for('tasks'))

        error = 'Task\'s description can\'t be empty'

    db = get_db()
    tasks = db.execute('SELECT * FROM tasks ORDER BY added_at DESC;').fetchall()
    return render_template('task_list.html', tasks=tasks, error=error)

@app.route('/done', methods=['POST'])
def mark_as_done():
    task_id = request.form['id']
    db = get_db()
    db.execute('UPDATE tasks SET done=1 WHERE id=?', [task_id])
    db.commit()
    flash('Status changed!')

    return redirect (url_for('tasks'))

if (__name__ == '__main__'):
    app.run(debug=True)