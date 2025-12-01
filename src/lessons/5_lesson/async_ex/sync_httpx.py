# pip install httpx / poetry add httpx
import time

import httpx
from urls import urls

"""
Синхронный вариант:
- httpx.Client() - обычный синхронный HTTP-клиент
- запросы выполняются последовательно
"""


def fetch(url):
    with httpx.Client() as client:
        try:
            response = client.get(url)
            print(f'{url}: {len(response.text)} bytes')
        except httpx.RequestError:
            print(f'Error fetching {url}: timeout')


def main():
    for url in urls:
        fetch(url)  # выполняем запрос по очереди


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'\nSynchronous code was executed in {time.time() - start:.2f} seconds')  # ~8 секунды
