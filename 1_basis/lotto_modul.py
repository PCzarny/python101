import random
import os
import json

def read_settings(filename):
    if os.path.isfile(filename):
        file = open(filename, 'r')
        line = file.readline()
        file.close()
        if line:
            return line.split(';')
    return False

def save_settings(filename, user):
    file = open(filename, 'w')
    file.write(";".join(user))
    file.close()

def settings():
    """This function ask user about number of numbers that should be picked
    and max value."""

    nick = input("Provide nick: ")
    filename = nick + '.ini'

    user = read_settings(filename)
    confirmation = None

    if user:
        print(f'Your settings:\nNumbers: {user[1]}\n Max: {user[2]}\n Tries: {user[3]}')
        confirmation = input('Do you want to change (y/n)? ')

    if not user or confirmation.lower() == 'y':
        while True:
            try:
                numbers_size = int(input('Define number of random numbers: '))
                range_max = int(input('Define max value: '))

                if numbers_size > range_max:
                    raise ValueError

                try_number = int(input("How many tries: "))
                break
            except ValueError:
                print('Invalida data!')
                continue
        user = [nick, str(numbers_size), str(range_max), str(try_number)]
        save_settings(filename, user)
    return user[0:1] + [int(x) for x in user[1:4]]

def get_randoms(size, range_max):
    """This function generate list of unique random numbers"""

    numbers = []
    i = 0

    while i < size:
        number = random.randint(1, range_max)
        if numbers.count(number) == 0:
            numbers.append(number)
            i = i + 1
    return numbers

def get_answers (size, range_max):
    """Function gets user's answers"""
    print(f'Define {size} from {range_max} numbers')

    answers = set()

    while len(answers) < size:
        try:
            answer = int(input(f'Define {len(answers) + 1}. number'))
        except ValueError:
            print('Invalid data!')
            continue

        if 0 < answer <= range_max and answers not in answers:
            answers.add(answer)

    return answers

def results (randoms, answers):
    hits = set(randoms) & answers

    if hits:
        print(f'\nYou\'ve hit {len(hits)} numbers:', ", ".join(map(str, hits)))
    else:
        print('You\'ve missed')
    return len(hits)

def read_json(filename):
    data = []
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    return data

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)