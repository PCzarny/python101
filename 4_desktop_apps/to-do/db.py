from peewee import *
from datetime import datetime

base = SqliteDatabase('adressess.db')
fields = ['Id', 'Description', 'Add date', 'Is done', 'Remove']

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

def parseTask (task):
    return [
        task.id,
        task.description,
        '{0:%Y-%m-%d %H:%M:%S}'.format(task.date),
        task.isCompleted,
        False]

def readData(person):
    tasks = Task.select().where(Task.assigned == person)
    return list(map(parseTask, tasks))

def addTask(person, description):
    task = Task(description=description, assigned=person, )
    task.save()
    return parseTask(task)

def saveData(tasks):
    for i, task in enumerate(tasks):
        model = Task.select().where(Task.id == task[0]).get()
        if task[4]:
            model.delete_instance()
            del tasks[i]
        else:
            model.description = task[1]
            model.isCompleted = task[3]
            model.save()
