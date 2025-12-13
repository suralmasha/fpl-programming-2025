from collections.abc import Iterator


class Counter:
    """Протокол итерации"""

    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._current = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:  # конкретно тут int
        if self._current >= self._limit:
            raise StopIteration
        self._current += 1

        return self._current


if __name__ == '__main__':
    """
    В протоколе контейнера обычно `__iter__()` возвращает новый итератор
    В протоколе итерации обычно `__iter__()` возвращает `self`

    `for x in obj`
    - Python вызывает `obj.__iter__()`
    - Получает итератор
    - Повторно вызывает `__next__()`
    - Остановка - по `StopIteration`

    Если у объекта нет `__iter__`, Python пробует:
    `obj[0], obj[1], obj[2], ...`, т.е. вызывает `obj.__getitem__(0), obj.__getitem__(1), ...`,
    пока не получит `IndexError`

    Почему бы не использовать только `__getitem__()`?
    - Нет явного конца (только через `IndexError`)
    - Нельзя корректно сделать бесконечную последовательность
    - Нет отдельного объекта-итератора
    - Не соответствует протоколу
    - Да и вообще считается устаревшим
    """
    for x in Counter(3):
        print(x)

    print()
    c = Counter(3)
    for x in c:
        print(x)

    print()
    print(c)
