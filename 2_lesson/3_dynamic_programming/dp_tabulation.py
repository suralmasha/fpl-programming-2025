import time


def fib_tab_optimized(n):
    """Вычисляет Фибоначчи с табуляцией и оптимизацией памяти до O(1)."""
    if n < 0:
        raise ValueError('N должно быть >= 0')
    if n <= 1:
        return n

    # Храним только два последних вычисленных значения
    prev2 = 0  # Соответствует fib(i-2), начинаем с fib(0)
    prev1 = 1  # Соответствует fib(i-1), начинаем с fib(1)

    # Итерируемся от 2 до n
    for i in range(2, n + 1):
        # Вычисляем текущее значение fib(i)
        current = prev1 + prev2

        # Сдвигаем значения для следующей итерации:
        # то, что было prev1, станет prev2
        # то, что было current, станет prev1
        prev2 = prev1
        prev1 = current
        # print(f"Итерация {i}: current=fib({i})={current}, prev1={prev1}, prev2={prev2}")

    # После завершения цикла prev1 будет содержать fib(n)
    return prev1


if __name__ == '__main__':
    n_val_opt = 100
    print(f'\n--- Вычисляем fib({n_val_opt}) с оптимизированной табуляцией ---')
    start_time = time.perf_counter()
    result_opt = fib_tab_optimized(n_val_opt)
    end_time = time.perf_counter()
    print(f'fib({n_val_opt}) = {result_opt}')
    print(f'Время выполнения: {end_time - start_time:.6f} сек')  # Быстро, O(n) по времени
    print('Пространственная сложность: O(1)')  # Используем константное количество памяти!
