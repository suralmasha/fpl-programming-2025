from collections.abc import Iterator


class Bag:
    """Протокол контейнера"""

    def __init__(self, items: list) -> None:
        self._items = items

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> int:  # конкретно тут int
        return self._items[index]

    def __contains__(self, item: object) -> bool:
        return item in self._items

    def __iter__(self) -> Iterator:  # Рекомендуемый способ сделать контейнер итерируемым
        return iter(self._items)


if __name__ == '__main__':
    bag = Bag([1, 2, 3, 4])
    bag_2 = Bag([])

    print(f'{len(bag) = }')  # 4
    print(f'{bool(bag) = }')  # True
    print(f'{bool(bag_2) = }')  # False

    print(f'\n{bag[1] = }')  # 2
    print(f'{bag[1:3] = }')  # [2, 3]

    print(f'\n{1 in bag}')  # True
    print(f'{5 in bag}')  # False
    
    print()
    for x in bag:  # -> __iter__
        print(x)
