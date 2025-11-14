import time

# КРАЙНЕ НЕЭФФЕКТИВНАЯ наивная рекурсия для Фибоначчи
def fib_naive(n):
    print(f"Вычисляем fib_naive({n})")
    if n < 0:
        raise ValueError("N должно быть >= 0")
    if n <= 1:
        return n
    else:
        # Вот здесь проблема: fib(n-1) и fib(n-2) будут многократно
        # вызывать вычисление ОДНИХ И ТЕХ ЖЕ меньших значений fib(k)
        return fib_naive(n - 1) + fib_naive(n - 2)

if __name__ == "__main__":
    n_val = 30
    print(f"Вычисляем fib({n_val}) наивной рекурсией (может занять время)...")
    start_time = time.perf_counter()
    try:
        result_naive = fib_naive(n_val)
        end_time = time.perf_counter()
        print(f"fib({n_val}) = {result_naive}")
        print(f"Время выполнения: {end_time - start_time:.6f} сек")
    except ValueError as e:
        print(e)
    except RecursionError:
        print("Ошибка: Достигнута максимальная глубина рекурсии!")


    """
                fib(5)
               /      \
            fib(4)     fib(3)  <-- fib(3) вызывается 1 раз здесь
           /     \       /     \
        fib(3) fib(2) fib(2) fib(1) <-- fib(3) вызывается еще 1 раз, fib(2) - 2 раза
       /    \    / \   / \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0) <-- fib(2) вызывается еще раз...
     / \
    fib(1) fib(0)
    
    """
    # Количество вызовов растет экспоненциально - примерно как O(2^n)
