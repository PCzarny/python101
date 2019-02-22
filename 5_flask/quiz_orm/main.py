import os
from app import app, base
from models import *
from views import *
from data import *

if __name__ == '__main__':
  if not os.path.exists(app.config['DATABASE']):
    base.create_tables([Question, Answer], safe=True)
    add_questions(load_data('data.csv'))
  app.run(debug=True)
