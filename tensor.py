import math
from typing import List, Tuple, Union


def unary_operation(a, op):
    return [op(x) for x in a]


def binary_operation(a, b, op):
    return [op(x, y) for x, y in zip(a, b)]


class Vector(object):
    def __init__(self, data: List[float]):
        self.data = data

    @property
    def shape(self) -> Tuple[int, ...]:
        return self.data.__len__(),

    def __repr__(self):
        return f'{self.data}'

    def __neg__(self) -> 'Vector':
        return Vector(unary_operation(self.data, lambda x: -x))

    def __add__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: x + other))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: x + y))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __radd__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: other + x))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: y + x))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __sub__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: x - other))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: x - y))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __rsub__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: other - x))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: y - x))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __mul__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: x * other))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: x * y))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __rmul__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: other * x))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: y * x))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: x / other))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: x / y))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __rtruediv__(self, other):
        if isinstance(other, float):
            return Vector(unary_operation(self.data, lambda x: other / x))
        elif isinstance(other, Vector):
            return Vector(binary_operation(self.data, other.data, lambda x, y: y / x))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def __matmul__(self, other: 'Vector') -> float:
        if isinstance(other, Vector):
            return sum(binary_operation(self.data, other.data, lambda x, y: x * y))
        else:
            raise TypeError(f'unsupported type :: {type(other)}')

    def log(self) -> 'Vector':
        return Vector(unary_operation(self.data, math.exp))

    def sum(self) -> float:
        return sum(self.data)

    def mean(self) -> float:
        return sum(self.data) / len(self.data)


class Matrix(object):
    def __init__(self, data: List[List[float]]):
        self.data = data

    @property
    def shape(self) -> Tuple[float, ...]:
        return self.data.__len__(), self.data[0].__len__()

    def __repr__(self):
        return f'{self.data}'

    def __neg__(self) -> 'Matrix':
        return Matrix(unary_operation(
            self.data, lambda row: unary_operation(row, lambda x: -x)))

    def __add__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: x + other)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: x + y)
            ))

    def __radd__(self, other):
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: other + x)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: y + x)
            ))

    def __sub__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: x - other)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: x - y)
            ))

    def __rsub__(self, other):
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: other - x)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: y - x)
            ))

    def __mul__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: x * other)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: x * y)
            ))

    def __rmul__(self, other):
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: other * x)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: y * x)
            ))

    def __truediv__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: x / other)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: x / y)
            ))

    def __rtruediv__(self, other):
        if isinstance(other, float):
            return Matrix(unary_operation(
                self.data, lambda row: unary_operation(row, lambda x: other / x)
            ))
        else:
            return Matrix(binary_operation(
                self.data, other.data, lambda r1, r2: binary_operation(r1, r2, lambda x, y: y / x)
            ))

    def __matmul__(self, other: Union['Vector', 'Matrix']) -> Union['Vector', 'Matrix']:
        if isinstance(other, Vector):
            return Vector([
                sum(binary_operation(row, other.data, lambda x, y: x * y))
                for row in self.data
            ])
        else:
            return Matrix([
                [sum(binary_operation(row, col, lambda x, y: x * y)) for col in zip(*other.data)]
                for row in self.data
            ])

    @property
    def T(self) -> 'Matrix':
        return Matrix(list(zip(*self.data)))

    def sum(self, axis: int) -> Union[float, Vector]:
        if axis is None:
            return sum(sum(row) for row in self.data)
        elif axis == 0:
            return Vector([sum(row) for row in self.data])
        elif axis == 1:
            return Vector([sum(col) for col in zip(*self.data)])
        else:
            raise ValueError(f'unsupported axis :: {axis}')

    def mean(self, axis: int) -> Union[float, Vector]:
        if axis is None:
            return self.sum(axis) / len(self.data) * len(self.data[0])
        elif axis == 0:
            return self.sum(axis) / len(self.data[0])
        elif axis == 1:
            return self.sum(axis) / len(self.data)
        else:
            raise ValueError(f'unsupported axis :: {axis}')


def sigmoid(inputs: Vector) -> Vector:
    return Vector(unary_operation(inputs.data, lambda x: 1.0 / (1.0 + math.exp(-x))))
