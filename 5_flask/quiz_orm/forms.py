from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms.validators import Required

error1 = 'This field is required'
error2 = 'Correct answer is missing'

class AddForm(FlaskForm):
    question = StringField('Question:',
                            validators=[Required(message=error1)])
    answers = FieldList(StringField(
                        'Answer',
                        validators=[Required(message=error1)]),
                        min_entries=3,
                        max_entries=3)
    correct = RadioField(
        'Correct answer',
        validators=[Required(message=error2)],
        choices=[('0', 'a0'), ('1', 'a1'), ('2', 'a2')]
    )
    question_id = HiddenField('Question id')