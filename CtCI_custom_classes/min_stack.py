from CtCI_Custom_Classes.stack import Stack


class StackWithMin(Stack):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.stack_min = Stack(capacity)

    def push(self, data):
        if self.get_size() == 0:
            self.stack_min.push(data)
        else:
            self.stack_min.push(min(self.stack_min.peek(), data))
        super().push(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        self.stack_min.pop()
        super().pop()

    def get_min(self):
        """
        return min of stack
        :return: min of stack
        """
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        return self.stack_min.peek()
