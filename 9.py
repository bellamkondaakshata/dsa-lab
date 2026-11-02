class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def height(self, node):
        if not node:
            return 0
        return node.height
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        # Perform rotation
        x.right = y
        y.left = T2
        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        # Return new root
        return x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        # Perform rotation
        y.left = x
        x.right = T2
        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        # Return new root
        return y
    def insert(self, root, key):
        # 1. Standard BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed
        # 2. Update height of this ancestor node
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # 3. Get the balance factor
        balance = self.get_balance(root)
        # 4. If the node becomes unbalanced, then 4 cases:
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    def delete(self, root, key):
        # 1. Standard BST delete
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        if not root:
            return root
        # 2. Update height
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # 3. Get balance factor
        balance = self.get_balance(root)
        # 4. Balance the tree if needed
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def pre_order(self, root):
        if not root:
            return []
        return [root.key] + self.pre_order(root.left) + self.pre_order(root.right)
# --- Example Usage ---
if __name__ == "__main__":
    avl = AVLTree()
    root = None
    # Insert elements
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        root = avl.insert(root, el)
    print("Preorder traversal of constructed AVL tree:")
    print(avl.pre_order(root))
    # Delete element
    root = avl.delete(root, 40)
    print("\nPreorder traversal after deletion of 40:")
    print(avl.pre_order(root))
