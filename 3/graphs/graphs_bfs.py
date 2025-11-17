from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # Список смежности

    def add_edge(self, u, v, is_directed=False):
        """Добавляет ребро между u и v."""
        self.graph[u].append(v)
        if not is_directed:
            self.graph[v].append(u) # Для неориентированного

    def bfs(self, start_node):
        """Выполняет BFS графа, начиная с start_node."""
        if start_node not in self.graph:
            print(f"Стартовая вершина {start_node} отсутствует.")
            return []

        visited = ...
        queue = ...
        result_order = [] # Список для хранения порядка обхода

        while queue:
            current_node = ...
            ...

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    ...

        print(f"BFS от {start_node}: {result_order}")

        return result_order


"""
Алгоритм BFS:
1) Выбрать стартовую вершину `s`
2) Создать пустую очередь `queue` и добавить в неё `s`
3) Создать пустое множество `visited` и добавить в него `s`
4) Пока `queue` не пуста:
    a) Извлечь вершину `u` из начала `queue`
    b) Добавить `u` в результат
    c) Для каждого соседа `v` вершины `u`:
        d) Если `v` не в `visited`, добавить `v` в `visited` и добавить `v` в конец `queue`.
"""

if __name__ == '__main__':
    # --- Создаем граф (ориентированный) ---
    # 0 -> 1, 0 -> 2
    # 1 -> 2
    # 2 -> 0, 2 -> 3
    # 3 -> 3
    g_bfs = Graph()
    g_bfs.add_edge(0, 1, is_directed=True)
    g_bfs.add_edge(0, 2, is_directed=True)
    g_bfs.add_edge(1, 2, is_directed=True)
    g_bfs.add_edge(2, 0, is_directed=True)  # Цикл!
    g_bfs.add_edge(2, 3, is_directed=True)
    g_bfs.add_edge(3, 3, is_directed=True)  # Петля!

    g_bfs.bfs(2)  # [2, 0, 3, 1]
