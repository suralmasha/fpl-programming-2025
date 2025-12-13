from types import TracebackType
from typing import TextIO


class FileManager:
    """Протокол контекстного менеджера"""

    def __init__(self, path: str) -> None:
        self._path = path

    def __enter__(self) -> TextIO:
        self.file = open(self._path, 'w')

        return self.file

    def __exit__(
            self,
            exc_type: type(BaseException) | None,
            exc: BaseException | None,
            tb: TracebackType | None
    ) -> bool:
        self.file.close()

        # return exc_type is ValueError
        return False


if __name__ == '__main__':
    with FileManager('file.txt') as f:
        # raise ValueError('invalid file content')
        f.write('hello\n')
    