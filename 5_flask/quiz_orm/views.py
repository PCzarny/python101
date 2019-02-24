from flask import render_template, request, redirect, url_for, abort, flash
from app import app
from models import Question, Answer
from forms import AddForm
from peewee import prefetch

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/list')
def question_list():
    questions = prefetch(Question().select(), Answer)
    if not len(questions):
        flash('No question', 'kom')
        return redirect(url_for('index'))

    return render_template('list.html', questions=questions)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for question_id, answer in request.form.items():
            correct = Question.select(Question.correct).where(Question.id == int(question_id)).scalar()
            if answer == correct:
                score +=1
        flash('Your score: {0}'.format(score))
        return redirect(url_for('index'))

    questions = prefetch(Question().select(), Answer)
    if not len(questions):
        flash('No question', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', questions=questions)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash('Error: {}. Field: {}'.format(
                error,
                getattr(form, field).label.text
            ))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        answers = form.answers.data
        question = Question(question=form.question, correct=answers[int(form.correct)])
        question.save()

        for answer in answers:
            Answer(question_id=question.id, answer=answer)
        flash('Question added: {}'.format(form.question.data))
        return redirect(url_for('question_list'))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template('add.html', form=form, radio=list(form.correct))

def get_or_404(question_id):
    try:
        return prefetch(Question().select().where(Question.id == question_id), Answer)[0]
    except Question.DoesNotExist:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/edit/<int:question_id>', methods=['GET', 'POST'])
def edit(question_id):
    question = get_or_404(question_id)
    form = AddForm()

    if form.validate_on_submit():
        new_answers = form.answers.data

        question.question = form.question.data
        question.correct = new_answers[int(form.correct.data)]
        question.save()

        for i, ans in enumerate(question.answers):
            ans.answer = new_answers[i]
            ans.save()

        flash('Question updated: {}'.format(form.question.data))
        return redirect(url_for('question_list'))
    elif request.method == 'POST':
        flash_errors(form)

    for i in range(3):
        if question.correct == question.answers[i].answer:
            question.correct = i
            break
    form = AddForm(obj=question)
    return render_template('edit.html', form=form, radio=list(form.correct))

@app.route('/delete/<int:question_id>', methods=['GET', 'POST'])
def delete(question_id):
    q = get_or_404(question_id)
    if request.method == 'POST':
        flash('Question {0} removed'.format(q.question), 'success')
        q.delete_instance(recursive=True)
        return redirect(url_for('index'))
    return render_template('delete_question.html', question=q)
