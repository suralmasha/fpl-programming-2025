from math import sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector(x={self.x}, y={self.y})'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        # `object`, потому что `==` может сравнивать с чем угодно
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        # len() должен возвращать int -> жесткий протокол
        return int(sqrt(self.x ** 2 + self.y ** 2))

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        if index == 1:
            return self.y

        raise IndexError('Vector supports only indices 0 and 1')


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f'{v1 = }')  # __str__ -> (3, 4)
    print(f'{repr(v1) = }')  # __repr__ -> Vector(x=3, y=4)

    print(f'\n{v1 + v2 = }')  # __add__ -> (4, 6)
    # print(v1 + 2)  # TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
    # print(2 + v1)  # TypeError: unsupported operand type(s) for +: 'int' and 'Vector'

    print(f'\n{v1 == v2 = }')  # __eq__ -> False
    print(f'{v1 == (3, 4) = }')  # __eq__ -> False
    print(f'{v1 == Vector(3, 4) = }')  # __eq__ -> True

    print(f'\n{len(v1) = }')  # __len__ -> 5

    print(f'\n{v1[0] = }')  # __getitem__ -> 3
    print(f'{v1[1] = }')  # __getitem__ -> 4
    # print(v1[2])  # __getitem__ -> IndexError: Vector supports only indices 0 and 1
    
    print('\nИтерация:')
    for x in v1:
        print(x)

