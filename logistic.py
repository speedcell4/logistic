from tensor import Vector, Matrix, sigmoid
from random import random
from data_loader import prepare, data_iteration


class Classifier(object):
    def __init__(self, input_size: int):
        self.input_size = input_size

        self.W = Vector([random() / (input_size ** 0.5) for _ in range(input_size)])
        self.b = Vector([0.])

    def forward(self, datum) -> Vector:
        return sigmoid(datum @ self.W)

    def backward(self, datum, output, target) -> Vector:
        return datum.T @ (target - output)


def loss(output, target) -> float:
    return (target * output.log() + (1. - target) * (1. - output).log()).mean()


def accuracy(output, target) -> float:
    x = [int(y >= 0.5) == int(t) for y, t in zip(output.data, target.data)]
    return sum(x) / len(x)


def train(vocab_size: int = 1000, num_epochs: int = 20, batch_size: int = 32, learning_rate: float = 0.05):
    data, targets = prepare(vocab_size, False)
    logistic = Classifier(vocab_size)

    for epoch in range(num_epochs):
        for datum, target in data_iteration(data, targets, batch_size):
            datum = Matrix(datum)
            target = Vector(target)

            output = logistic.forward(datum)

            grad = logistic.backward(datum, output, target)
            logistic.W += grad * learning_rate

        outputs = logistic.forward(Matrix(data))
        acc = accuracy(outputs, Vector(targets))
        l = loss(outputs, Vector(targets))
        print(f'acc => {acc:.2f}, loss => {l:.2f}')


if __name__ == '__main__':
    train()
