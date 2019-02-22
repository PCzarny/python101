import os
import csv
from models import Question, Answer

def load_data(filename):
  """Function return tuple that  include tuples with data from file"""
  data = []
  if os.path.isfile(filename):
    with open(filename, newline='') as file:
      content = csv.reader(file, delimiter='#')
      for record in content:
        data.append(tuple(record))
  else:
    print('File does not exist')

  return data

def add_questions(data):
  for question, answers, correct in data:
    q = Question(question=question, correct=correct)
    q.save()

    for answer in answers.split(','):
      ans = Answer(question_id=q.id, answer=answer.strip())
      ans.save()

  print('Sample data we added')