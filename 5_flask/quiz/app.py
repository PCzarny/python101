from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secretKey'
))

DATA = [{
    'question': 'Capitol city of Spain',
    'answers': ['Madrit', 'Warsaw', 'Barcelona'],
    'correct': 'Madrit'
}]

@app.route('/')
def index() :
    return render_template('index.html', questions=DATA)

@app.route('/hello')
def hello() :
    return 'Hello it\'s Python'

if (__name__ == '__main__'):
    app.run(debug=True)