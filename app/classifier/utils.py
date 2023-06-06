"""
Utilities.
"""
import json


def train_test_split(data):
    x_train, x_test, y_train, ids = [], [], [], []
    for d in data:
        text = d['text']
        if d['manual']:
            x_train.append(text)
            label = d['label']
            y_train.append(label)
        else:
            x_test.append(text)
            ids.append(d['id'])

    return x_train, x_test, y_train, ids


def load_dataset(filename):
    with open(filename) as f:
        data = [json.loads(line) for line in f]

    return data


def save_dataset(obj, filename):
    with open(filename, 'w') as f:
        for line in obj:
            f.write(f'{json.dumps(line)}\n')


def make_output(data, ids, y_pred, y_prob):
    i = 0
    for d in data:
        if i == len(ids):
            break
        if d['id'] == ids[i]:
            d['label'] = str(y_pred[i])
            d['prob'] = float(y_prob[i])
            i += 1

    return data
