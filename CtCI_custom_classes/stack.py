from CtCI_Custom_Classes.node import Node


class Stack:
    """
    Implementation of LIFO stack, with a limit to size
    """
    def __init__(self, capacity):
        self.head = Node('head')
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        current = self.head.get_next()
        out = ""
        while current:
            out += str(current.get_value()) + " -> "
            current = current.get_next()
        return out[:-4]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.capacity

    def pop(self):
        """
        Remove top value from stack
        :return:
        """
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.get_next()
        self.head.set_next(self.head.get_next().get_next())
        self.size -= 1
        return remove.get_value()

    def push(self, data):
        """
        Add data to stack
        :param data: data to add
        :return: None
        """
        if self.is_full():
            raise Exception("Cannot add to a full stack")
        node = Node(data)
        node.set_next(self.head.get_next())
        self.head.set_next(node)
        self.size += 1

    def peek(self):
        """
        Look at the top value of the stack
        :return: top node value
        """
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.get_next().get_value()
