import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Creating connection
if os.path.exists('test.db'):
    os.remove('test.db')

base = create_engine('sqlite:///test.db')  # ':memory:'

BaseModel = declarative_base()

# Defining models
class Task(BaseModel):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), default='')
    project_id = Column(Integer, ForeignKey('projects.id'))

class Project(BaseModel):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    tasks = relationship('Task', backref='project')

# Creating tables
BaseModel.metadata.create_all(base)

# CRUD operations
DBSession = sessionmaker(bind=base)
session = DBSession()

if not session.query(Project).count():
    session.add(Project(title='Home'))
    session.add(Project(title='Work'))

home_project = session.query(Project).filter_by(title='Home').one()

session.add_all([
    Task(title='Shopping', project_id=home_project.id),
    Task(title='Washing dishes', project_id=home_project.id),
    Task(title='Cleaning', project_id=home_project.id),
])

def read_data():
    for task in session.query(Task).join(Project).all():
        print(task.id, task.title, task.project.title)
    print()

read_data()

# Modifing and removing data
task = session.query(Task).filter(Task.id == 2).one()
task.project_id = session.query(Project.id).filter(Project.title == 'Work').scalar()

session.delete(session.query(Task).get(3))

read_data()

session.commit()
session.close()