import time
from lotto_modul import settings, get_randoms, get_answers, results, read_json, write_json

def main(args):
    nick, numbers_size, range_max, try_number = settings()

    randoms = get_randoms(numbers_size, range_max)

    for trial in range(try_number):
        answers = get_answers(numbers_size, range_max)
        score = results(randoms, answers)

    filename = nick + '.json'
    history = read_json(filename)
    history.append({
        "time": time.time(),
        "data": (numbers_size, range_max),
        "solution": randoms,
        "score": score
    })

    write_json(filename, history)

    print('Solution:', randoms)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))