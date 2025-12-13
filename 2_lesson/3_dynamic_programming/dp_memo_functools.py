import functools
import time

# import sys
# При необходимости можно увеличить лимит рекурсии, но кеш часто помогает
# sys.setrecursionlimit(2000)


# Используем декоратор @cache (для Python 3.9+)
# или @functools.lru_cache(maxsize=None) для более старых версий
@functools.cache
def fib_cached(n):
    """Вычисляет Фибоначчи с автоматической мемоизацией через @cache."""
    print(f'Вызов fib_cached({n})')
    if n < 0:
        raise ValueError('N должно быть >= 0')
    if n <= 1:
        return n
    else:
        return fib_cached(n - 1) + fib_cached(n - 2)


if __name__ == '__main__':
    n_val_cache = 100  # Теперь можно брать n побольше!
    print(f'\n--- Вычисляем fib({n_val_cache}) с @cache ---')
    start_time = time.perf_counter()
    result_cache = fib_cached(n_val_cache)
    end_time = time.perf_counter()
    print(f'fib({n_val_cache}) = {result_cache}')
    print(f'Время выполнения: {end_time - start_time:.6f} сек')

    # Декоратор предоставляет удобный способ посмотреть статистику кеша
    print(f'Статистика кеша fib_cached: {fib_cached.cache_info()}')
    # hits - сколько раз результат взят из кеша
    # misses - сколько раз результат пришлось вычислить
    # currsize - текущий размер кеша
