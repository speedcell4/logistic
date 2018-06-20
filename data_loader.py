from collections import Counter
from pathlib import Path
from random import shuffle

project_dir = Path(__file__).expanduser().absolute().parent
positive = project_dir / 'data' / 'data' / 'books' / 'positive.review'
negative = project_dir / 'data' / 'data' / 'books' / 'negative.review'


def sentence_stream(path: Path):
    with path.open('r', encoding='utf-8') as reader:
        for raw_line in reader:
            sentence = []
            for item in raw_line.strip().split():
                token, freq = item.split(':')
                try:
                    sentence.append((token, int(freq)))
                except ValueError:
                    print(token, freq)
                    exit(1)
            yield sentence


def update_counter(path: Path, counter: Counter):
    for sentence in sentence_stream(path):
        for token, freq in sentence:
            counter[token] += freq


def build_vocabulary(vocab_size: int):
    counter = Counter()
    update_counter(positive, counter)
    update_counter(negative, counter)

    vocabulary = {}
    for ix, (token, _) in enumerate(counter.most_common(vocab_size)):
        vocabulary[token] = ix

    return vocabulary


def prepare(vocab_size: int, debug: bool):
    vocabulary = build_vocabulary(vocab_size)
    print(f'vocabulary size => {vocabulary.__len__()}')

    def handle(path: Path, target: float):
        for sentence in sentence_stream(path):
            datum = [0] * vocabulary.__len__()
            for token, freq in sentence:
                if token in vocabulary:
                    datum[vocabulary[token]] = 1
            yield datum, target
            if debug:
                break

    pos_data, pos_targets = zip(*handle(positive, 1.0))
    neg_data, neg_targets = zip(*handle(negative, 0.0))
    dataset = list(zip(pos_data + neg_data, pos_targets + neg_targets))
    shuffle(dataset)
    data, targets = zip(*dataset)
    return data, targets


def data_iteration(data, targets, batch_size: int):
    for index in range((data.__len__() + batch_size - 1) // batch_size):
        yield data[batch_size * index:batch_size * (index + 1)], \
              targets[batch_size * index:batch_size * (index + 1)]


if __name__ == '__main__':
    data, targets = prepare(200, True)
    print('data', data.__len__())
    print('targets', targets.__len__())
