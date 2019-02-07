from peewee import *
from datetime import datetime

base = SqliteDatabase('adressess.db')

class BaseModel(Model):

    class Meta:
        database = base

class Person(BaseModel):
    login = CharField(null=False, unique=True)
    password = CharField()

    class Meta:
        order_by = ('login',)

class Task(BaseModel):
    description = TextField(null=False)
    date = DateTimeField(default=datetime.now)
    isCompleted = BooleanField(default=False)
    assigned = ForeignKeyField(Person, related_name='task')

    class Meta:
        order_by= ('date',)

def connect():
    base.connect()
    base.create_tables([Person, Task], safe=True)
    loadData()
    return True

def signin(login, password):
    try:
        person, _created = Person.get_or_create(login=login, password=password)
        return person
    except IntegrityError:
        return None

def loadData():
    if Person.select().count() > 0:
        return
    persons = ('Adam', 'Ewa')
    tasks = ('1. Task', '2. Task', '3. Task')

    for login in persons:
        person = Person(login=login, password='123')
        person.save()

        for description in tasks:
            task = Task(description=description, assigned=person)
            task.save()
    base.commit()
    base.close()