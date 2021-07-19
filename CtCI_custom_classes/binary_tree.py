from collections import deque


class BinaryTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_left(self):
        return self.left

    def set_left(self, key):
        self.left = key

    def get_right(self):
        return self.right

    def set_right(self, key):
        self.right = key

    def __repr__(self):
        return f'{self.key} l: {self.left} r: {self.right}'

    def __eq__(self, other):
        if self.get_key() == other.get_key() and \
            self.get_right() == other.get_right() and \
                self.get_left() == other.get_left():
            return True
        else:
            return False


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, key):
        self.root = key

    def __repr__(self):
        return str(self.traverse_inorder(self.get_root()))

    def __str__(self, level=0, depth=0):
        if depth == 0:
            depth = self.get_depth()
        ret = '\t' * level + repr(self.get_root()) + ('___' * depth) + '\n'
        for child in self.traverse_inorder(self.get_root()):
            if child is None:
                ret += ("\t" * (level+1)) + '|\n'
            else:
                ret += child.__str__(level + 1, depth - 1)
        return ret

    def get_depth(self):
        d = 1
        if self.traverse_inorder(self.get_root()) is None:
            return d
        for c in self.traverse_inorder(self.get_root()):
            if c is not None:
                d = max(d, c.get_depth() + 1)
        return d

    def add(self, value):
        new = BinaryTreeNode(value)
        if self.get_root() is None:
            self.set_root(new)
        else:
            self._add(value, self.get_root())

    def _add(self, value, node):
        new = BinaryTreeNode(value)
        if value < node.get_key():
            if node.get_left() is not None:
                self._add(value, node.get_left())
            else:
                node.set_left(new)
        else:
            if node.get_right() is not None:
                self._add(value, node.get_right())
            else:
                node.set_right(new)

    def find(self, value):
        if self.get_root() is not None:
            return self._find(value, self.get_root())
        else:
            return None

    def _find(self, value, node):
        if value == node.get_key():
            return node
        elif value < node.get_key() and node.get_left() is not None:
            return self._find(value, node.get_left())
        elif value > node.get_key() and node.get_right() is not None:
            return self._find(value, node.get_right())

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.get_root() is not None:
            self._print_tree(self.get_root())

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.get_left())
            print(str(node.get_key()) + ' ')
            self._print_tree(node.get_right())

    def bfs(self, node):
        if not node and self.find(node.get_key()):
            return
        reachable = []
        q = deque()
        q.append(node)
        while len(q):
            visit = q.popleft()
            reachable.append(visit)
            if visit.left:
                q.append(visit.left)
            if visit.right:
                q.append(visit.right)
        return reachable

    def dfs(self, node):
        if not node and self.find(node.get_key()):
            return
        reachable = []
        q = deque()
        q.append(node)
        while len(q):
            visit = q.pop()
            reachable.append(visit)
            if visit.left:
                q.append(visit.left)
            if visit.right:
                q.append(visit.right)
        return reachable

    def traverse_inorder(self, node, reachable=None):
        if node and self.find(node.get_key()):
            return
        if reachable is None:
            reachable = []
        self.traverse_inorder(node.get_left(), reachable)
        reachable.append(node.get_key())
        self.traverse_inorder(node.get_right(), reachable)
        return reachable

    def traverse_postorder(self, node, reachable=None):
        if node and self.find(node.get_key()):
            return
        if reachable is None:
            reachable = []
        self.traverse_postorder(node.get_left(), reachable)
        self.traverse_postorder(node.get_right(), reachable)
        reachable.append(node.get_key())
        return reachable

    def traverse_preorder(self, node, reachable=None):
        if node and self.find(node.get_key()):
            return
        if reachable is None:
            reachable = []
        reachable.append(node.get_key())
        self.traverse_preorder(node.get_left(), reachable)
        self.traverse_preorder(node.get_right(), reachable)
        return reachable
