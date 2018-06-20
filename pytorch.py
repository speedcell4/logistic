import numpy as np
import torch
from torch.nn import functional as F
from torch import nn, optim

from data_loader import data_iteration, prepare


class Classifier(nn.Module):
    def __init__(self, in_features: int, num_classes: int, bias: bool = True):
        super(Classifier, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(in_features, num_classes, bias=bias),
        )
        self.criterion = nn.CrossEntropyLoss()

    def forward(self, inputs):
        return self.net(inputs)

    def fit(self, inputs, targets):
        inputs = torch.from_numpy(np.array(inputs, dtype=np.float32))
        targets = torch.from_numpy(np.array(targets, dtype=np.int64))
        logits = self(inputs)
        predictions = F.softmax(logits, dim=-1).argmax(-1).long()

        loss = self.criterion(logits, targets)
        acc = (predictions == targets).float().mean()
        return loss, acc


def train(vocab_size: int = 1000, num_epochs: int = 20, batch_size: int = 32):
    data, targets = prepare(vocab_size=vocab_size, debug=False)
    model = Classifier(in_features=vocab_size, num_classes=2)
    optimizer = optim.Adam(model.parameters())

    for epoch in range(num_epochs):
        model.train()
        for datum, target in data_iteration(data, targets, batch_size=batch_size):
            loss, acc = model.fit(datum, target)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        loss, acc = model.fit(data, targets)
        print(f'acc => {acc.item():.2f}, loss => {loss.item():.2f}')


if __name__ == '__main__':
    train()
