from peewee import Model, CharField, ForeignKeyField
from app import base

class BaseModel(Model):
    class Meta:
        database = base

class Question(BaseModel):
    question = CharField(unique=True)
    correct = CharField()

    def __str__(self):
        return self.question

class Answer(BaseModel):
    question_id = ForeignKeyField(
        Question, related_name='answers', on_delete='CASCADE')
    answer = CharField()

    def __str__(self):
        return self.answer