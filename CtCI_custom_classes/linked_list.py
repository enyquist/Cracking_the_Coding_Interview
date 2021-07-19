from random import randint

from CtCI_custom_classes.node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def kth_to_last(self, k):
        current = runner = self.head
        for _ in range(k):
            if runner is None:
                return None
            runner = runner.get_next()

        while runner:
            current = current.get_next()
            runner = runner.get_next()

        return current.get_data()

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data is not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data is not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()

    def generate(self, length, start, stop):
        for _ in range(length):
            val = randint(a=start, b=stop)
            self.insert(val)
