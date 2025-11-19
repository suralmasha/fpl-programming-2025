def factorial_recursive(n):
    """Вычисляет факториал n с помощью рекурсии."""
    print(f'Вычисляем factorial_recursive({n})...')

    if not isinstance(n, int) or n < 0:
        raise ValueError('Факториал определен только для целых неотрицательных чисел')

    # 1. Базовый случай
    if n == 0 or n == 1:
        print(f'Базовый случай для n={n}, возвращаем 1.')
        return 1

    # 2. Рекурсивный шаг
    else:
        print(f'Рекурсивный шаг для n={n}. Вызываем factorial_recursive({n - 1}).')
        # Вызываем себя же для n-1
        result_n_minus_1 = factorial_recursive(n - 1)

        # Комбинируем результат
        result = n * result_n_minus_1
        print(f'Вернулись к n={n}. Результат {n} * factorial({n - 1}) = {result}')
        return result


if __name__ == '__main__':
    try:
        target_n = 4
        print(f'\n--- Запускаем вычисление {target_n}! ---')
        final_result = factorial_recursive(target_n)
        print('--- Готово ---')
        print(f'\nИтоговый факториал {target_n}! = {final_result}')
    except ValueError as e:
        print(f'Ошибка: {e}')

    # Попробуем некорректный ввод
    try:
        print('\n--- Пробуем factorial_recursive(-1) ---')
        factorial_recursive(-1)
    except ValueError as e:
        print(f'Ожидаемая ошибка: {e}')
