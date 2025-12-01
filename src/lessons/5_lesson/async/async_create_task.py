import asyncio
import time

"""
`async def` - функция, которая выполняется асинхронно
`await` - ждем завершения асинхронной операции - можно использовать только в асинхронной функции (под `async def`)
`asyncio.run()` - запускает асинхронный код в главном потоке

`asyncio.create_task(...)` - создаем задачу, которая запускается параллельно

Результат: обе задачи выполняются одновременно
"""


async def say_after(seconds, message):
    print(f'Start waiting {seconds} sec for {message}')
    await asyncio.sleep(seconds)
    print(message)
    print(f'Done waiting {seconds} sec for {message}')


async def main():
    task1 = asyncio.create_task(say_after(2, 'Hello'))
    task2 = asyncio.create_task(say_after(3, 'World'))

    print('Tasks started')
    await task1  # ждем завершения первой задачи
    await task2  # ждем завершения второй задачи
    print('All done')


if __name__ == '__main__':
    start = time.time()

    asyncio.run(main())

    print(f'\nCode was executed in {time.time() - start} seconds')  # ~3 секунды
