import random

try_number = 3

try:
    numbers_size = int(input('Define number of random numbers: '))
    range_max = int(input('Define max value: '))

    if numbers_size > range_max:
        raise ValueError
except ValueError:
    print('Invalida data!')
    exit()

numbers = []

i = 0
while i < numbers_size:
    number = random.randint(1, range_max)
    if numbers.count(number) == 0:
        numbers.append(number)
        i = i + 1

for trial in range(try_number):
    print(f'Define {numbers_size} from {range_max} numbers')
    answers = set()

    while len(answers) < numbers_size:
        try:
            answer = int(input(f'Define {len(answers) + 1}. number'))
        except ValueError:
            print('Invalid data!')
            continue

        if 0 < answer <= range_max and answers not in answers:
            answers.add(answer)

    hits = set(numbers) & answers
    if hits:
        print(f'\nYou\'ve hit {len(hits)} numbers:', hits)
    else:
        print('You\'ve missed')

    print("\n" + "x" * 40 + "\n")

print('Solution:', numbers)