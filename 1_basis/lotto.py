import random

solution = random.randint(1, 10)

try_number = 3
for i in range(try_number):
    print(f'Try number {i + 1}')
    answer = input('What number was chosen? ')

    if int(answer) == solution:
        print('Great! You won!')
        break
    elif i == try_number - 1:
        print(f'You\'ve lost. It was number {solution}')
    else:
        print(f'You\'ve missed. Try again\n')
