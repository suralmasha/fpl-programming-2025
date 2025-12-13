class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    # def __str__(self) -> str:
    #     return f'({self.x}, {self.y})'


if __name__ == '__main__':
    """
    `print()` вызывает встроенную функцию `str(obj)`
    `str(obj)` - если у объекта есть `__str__` → вызывает его, иначе → вызывает `__repr__`
    
    `__repr__` - должен быть максимально информативным (отладочное представление)
    `__str__`  - должен быть максимально читаемым (пользовательский вывод)
    """
    v1 = Vector(2, 3)
    v2 = Vector(10, 5)
    
    print(v1)  # Vector(2, 3) вместо <__main__.Vector object at 0x1008b5400>
    print(v2)  # Vector(10, 5)

    v3 = v1 + v2
    print(v3)   # Vector(12, 8)
    
    print([v1, v2, v3])  # список - протокол контейнера
