class Vector:
    """
    Двумерный вектор в декартовой системе координат.

    Поддерживает сложение векторов и строковые представления
    для отладки (`repr`) и пользовательского вывода (`str`).
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Инициализация вектора.

        :param x: Координата по оси X.
        :param y: Координата по оси Y.
        """
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Сложение двух векторов.

        :param other: Второй вектор для сложения.
        :return: Новый вектор, являющийся суммой текущего и переданного.
        :raises TypeError: Если сложение выполняется не с объектом Vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        """
        Формальное строковое представление вектора.

        Используется для отладки и в интерактивной оболочке.

        :return: Строка вида 'Vector(x, y)'.
        """
        return f'Vector({self.x}, {self.y})'

    def __str__(self) -> str:
        """
        Пользовательское строковое представление вектора.

        Используется при выводе через print().

        :return: Строка вида '(x, y)'.
        """
        return f'({self.x}, {self.y})'


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
