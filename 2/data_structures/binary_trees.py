from collections import deque


class TreeNode:
    """Представляет узел бинарного дерева."""
    def __init__(self, key):
        self.key = key     # Данные узла
        self.left = None   # Ссылка на левого потомка
        self.right = None  # Ссылка на правого потомка

    def __repr__(self):
        """Строковое представление узла (показывает ключ)."""
        return f"Node({self.key})"

def inorder(node):
    """
    In-order (LNR) обход.
    Сначала левое поддерево, потом узел, потом правое
    (идеально для получения отсортированной последовательности из BST - бинарного дерева поиска).
    Бинарное дерево поиска (BST) устроено так, что:
    - всё, что меньше узла, идёт влево,
    - всё, что больше, идёт вправо.
    """
    return inorder(node.left) + [node.key] + inorder(node.right) if node else []

def preorder(node):
    """
    Pre-order (NLR) обход.
    Сначала узел, потом левое, потом правое поддерево (полезно для копирования дерева, префиксной записи).
    """
    return [node.key] + preorder(node.left) + preorder(node.right) if node else []

def postorder(node):
    """
    Post-order (LRN) обход.
    Сначала левое, потом правое поддерево, потом узел (подходит для удаления узлов, постфиксной записи).
    """
    return postorder(node.left) + postorder(node.right) + [node.key] if node else []


def level_order(root):
    """BFS (Level-Order) обход."""
    if not root:
        return []
    result = []
    nodes_queue = deque([root])
    while nodes_queue:
        current_node = nodes_queue.popleft()
        result.append(current_node.key)
        if current_node.left:
            nodes_queue.append(current_node.left)
        if current_node.right:
            nodes_queue.append(current_node.right)
    return result


if __name__ == '__main__':
    # --- Тестовое дерево ---
    #       F
    #      / \
    #     B   G
    #    / \   \
    #   A   D   I
    #      / \   /
    #     C   E H

    root = TreeNode('F')
    root.left = TreeNode('B')
    root.right = TreeNode('G')
    root.left.left = TreeNode('A')
    root.left.right = TreeNode('D')
    root.left.right.left = TreeNode('C')
    root.left.right.right = TreeNode('E')
    root.right.right = TreeNode('I')
    root.right.right.left = TreeNode('H')

    print(f"In-order   (LNR): {inorder(root)}")  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    print(f"Pre-order  (NLR): {preorder(root)}")  # ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    print(f"Post-order (LRN): {postorder(root)}")  # ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

    print(f"Level-order (BFS): {level_order(root)}")  # ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
