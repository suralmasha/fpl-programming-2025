from collections import deque

queue_list = []
d = deque()

# Добавление элемента в правый конец
queue_list.append(10)  # O(1)
d.append(10)  # O(1)

# Удаление элемента из правого конца
x_from_l = queue_list.pop()  # O(1)
x_from_d = d.pop()  # O(1)

# Добавление элемента в левый конец
queue_list.insert(0, 20)  # O(n)
d.appendleft(20)  # O(1)

# Удаление элемента из левого конца
y_from_l = queue_list.pop(0)  # O(n)
y_from_d = d.popleft()  # O(1)
