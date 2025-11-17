import heapq


if __name__ == '__main__':
    # Очередь задач: (приоритет, описание). Меньше число = Высший приоритет.
    tasks_queue = []

    heapq.heappush(tasks_queue, (5, "Low priority task"))    # Низкий приоритет
    heapq.heappush(tasks_queue, (1, "Urgent bugfix"))   # Высший приоритет!
    heapq.heappush(tasks_queue, (3, "Write documentation")) # Средний приоритет
    heapq.heappush(tasks_queue, (1, "Reply to boss"))     # Тоже высший приоритет

    print(f"Текущая задача (высший приоритет, без извлечения): {tasks_queue[0]}") # O(1)

    print("Обработка задач по приоритету:")
    while tasks_queue:
        priority, task = heapq.heappop(tasks_queue) # Извлекаем с наименьшим приоритетом O(log n)
        print(f" - Приоритет {priority}: Выполняем '{task}'")
