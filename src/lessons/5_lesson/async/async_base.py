import asyncio
import time

"""
`async def` - функция, которая выполняется асинхронно
`await` - ждем завершения асинхронной операции - можно использовать только в асинхронной функции (под `async def`)
`asyncio.run()` - запускает асинхронный код в главном потоке

Результат: задачи выполняются последовательно, как обычный код
"""


# определяем асинхронную функцию
async def say_after(seconds, message):
    print(f'Start waiting {seconds} sec for {message}')
    await asyncio.sleep(seconds)  # ждем указанное время без блокировки потока
    print(message)
    print(f'Done waiting {seconds} sec for {message}')


async def main():
    await say_after(2, 'Hello')
    await say_after(3, 'World')


if __name__ == '__main__':
    start = time.time()

    asyncio.run(main())

    print(f'\nCode was executed in {time.time() - start} seconds')  # ~5 секунд
