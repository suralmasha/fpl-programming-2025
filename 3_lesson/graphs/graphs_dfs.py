from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.dfs_result_order = [] # Для хранения результата обхода

    def add_edge(self, u, v, is_directed=False):
        self.graph[u].append(v)
        if not is_directed:
            self.graph[v].append(u)

    # Вспомогательная рекурсивная функция
    def _dfs_recursive(self, vertex, visited):
        ...

        for neighbor in self.graph[vertex]:
            ...

    def dfs(self, start_node):
        """Выполняет DFS графа, начиная с start_node."""
        if start_node not in self.graph:
            print(f"Стартовая вершина {start_node} отсутствует.")
            return []

        visited = ...
        self.dfs_result_order = [] # Очищаем результат перед новым обходом
        self._dfs_recursive(start_node, visited)
        print(f"DFS от {start_node}: {self.dfs_result_order}")
        return self.dfs_result_order


"""
Алгоритм DFS:
1) Выбрать стартовую вершину `s`
2) Создать пустое множество `visited`
3) Вспомогательная рекурсивная функция:
    a) Пометить выбранную вершину как посещённую
    b) Добавить выбранную вершину в результат
    c) Для каждого соседа выбранной вершины:
        d) Если сосед не в `visited` - рекурсия
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

    g_bfs.dfs(2)  # [2, 0, 3, 1]
