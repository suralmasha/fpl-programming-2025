import time


def wait(seconds):
    print(f'Start waiting {seconds} sec')
    time.sleep(seconds)  # блокируем поток
    print(f'Done waiting {seconds} sec')


if __name__ == '__main__':
    start = time.time()

    wait(2)
    wait(3)

    print(f'\nCode was executed in {time.time() - start} seconds')  # ~5 секунд
