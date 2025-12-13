from typing import TextIO
from contextlib import contextmanager


"""
Декоратор `@contextmanager` позволяет написать контекстный менеджер без класса
и без явной реализации `__enter__` и `__exit__`
Он превращает генераторную функцию в объект, поддерживающий протокол контекстного менеджера

@contextmanager
def cm():
    ... # Вход в контекст - аналог `__enter__()`
    yield value  # То, что попадет в `as` - аналог возвращаемого значения `__enter__()`
    ... # Выход из контекста - аналог `__exit__()`
"""


@contextmanager
def file_manager(path: str) -> TextIO:
    file = open(path, 'w')
    yield file
    file.close()
    

"""
Если внутри `with` возникает исключение:
- выполнение прерывается
- управление возвращается в генератор в точку `yield`
- исключение пробрасывается внутрь генератора

def cm():
    ... # Вход в контекст - аналог `__enter__()`
    try:
        yield
    except exception:  # Подавление конкретного исключения
      ...
    finally:
    ... # Выход из контекста - аналог `__exit__()`
"""


@contextmanager
def file_manager_2(path: str) -> TextIO:
    file = open(path, 'w')
    try:
        yield file
    except ValueError:
        pass  # подавляем ValueError
    finally:
        file.close()
        
"""
Ограничения `@contextmanager`:
- Нельзя вызвать `yield` более одного раза
- Сложнее читать при большом количестве логики
- Не подходит, если нужно:
    - хранить состояние
    - иметь несколько методов
    - поддерживать вложенные режимы
"""


if __name__ == '__main__':
    with file_manager('file.txt') as f:
        # raise ValueError('invalid file content')
        f.write('hello\n')
    
    with file_manager_2('file.txt') as f:
        raise ValueError('invalid file content')
    