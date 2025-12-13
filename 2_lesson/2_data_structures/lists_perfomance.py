import time

n = 200000  # Достаточно большой размер для наглядности
print(f'\nСравнение производительности для {n} элементов:')

# --- Замеряем append (O(1) амортизированно) ---
big_list_append = []
start_time_append = time.perf_counter()  # Используем perf_counter для более точных замеров
for i in range(n):
    big_list_append.append(i)
end_time_append = time.perf_counter()
print(f' Время append {n} элементов: {end_time_append - start_time_append:.6f} сек')

# --- Замеряем insert(0, ...) (O(n)) ---
# Делаем в 10 раз меньше итераций, т.к. insert(0) намного медленнее!
iterations_insert = n // 10
big_list_insert = []
start_time_insert = time.perf_counter()
for i in range(iterations_insert):
    big_list_insert.insert(0, -i)  # Вставляем в начало
end_time_insert = time.perf_counter()
print(f' Время insert(0, ...) {iterations_insert} элементов: {end_time_insert - start_time_insert:.6f} сек')

# Очевидно, что insert(0,...) намного медленнее на больших n, даже при меньшем числе операций
