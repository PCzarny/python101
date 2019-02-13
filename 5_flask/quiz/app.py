from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secretKey'
))

DATA = [{
    'question': 'Capitol city of Spain',
    'answers': ['Madrit', 'Warsaw', 'Barcelona'],
    'correct': 'Madrit'
}]

@app.route('/', methods=['GET', 'POST'])
def index() :
    if request.method == 'POST':
        score = 0
        answers = request.form

        for i, answer in answers.items():
            if answer == DATA[int(i)]['correct']:
                score += 1
        flash('Your score: {0}'.format(score))
        return redirect(url_for('index'))
    return render_template('index.html', questions=DATA)

@app.route('/hello')
def hello() :
    return 'Hello it\'s Python'

if (__name__ == '__main__'):
    app.run(debug=True)