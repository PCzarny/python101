import os

def get_data(filename):
    data = []

    if os.path.isfile(filename):
        with open(filename, 'r') as content:
            for line in content:
                items = line.replace('\n', '') \
                    .replace('\r', '') \
                    .decode('utf-8') \
                    .split(',')
                data.append(tuple(items))
    else:
        print('File doesn\'t exist')
    return data