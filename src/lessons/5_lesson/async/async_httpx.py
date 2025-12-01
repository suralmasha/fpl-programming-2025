# pip install httpx / poetry add httpx
import asyncio
import time

import httpx

from .urls import urls

"""
`async def` - функция, которая выполняется асинхронно
`await` - ждем завершения асинхронной операции - можно использовать только в асинхронной функции (под `async def`)
`asyncio.run()` - запускает асинхронный код в главном потоке
`asyncio.create_task(...)` - создаем задачу, которая запускается параллельно

`httpx.AsyncClient()` - асинхронный HTTP-клиент
`async with` - асинхронный контекстный менеджер, гарантирует корректное закрытие соединения
`asyncio.gather(*tasks)` - ждем сразу все задачи

Результат: два запроса выполняются одновременно, вывод приходит быстрее, чем по очереди
"""


async def fetch(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            print(f'{url}: {len(response.text)} bytes')
        except httpx.RequestError:
            print(f'Error fetching {url}: timeout')


async def main():
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    await asyncio.gather(*tasks)  # запускаем все параллельно


if __name__ == '__main__':
    start_2 = time.time()
    asyncio.run(main())

    print(f'\nAsynchronous ccode was executed in {time.time() - start_2} seconds')  # ~5 секунд
