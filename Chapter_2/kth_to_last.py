"""
Task: Return Kth to Last
Implement an algorithm to find the Kth to alst element in a singly linked list
"""

from CtCI_custom_classes.linked_list import LinkedList


def kth_to_last(ll, k):
    """
    Function to return the kth to last element in a singly linked list
    :param ll: LinkedList object
    :param k: kth element
    :return: value at kth element
    """
    runner = current = ll.head
    for _ in range(k):
        if runner is None:
            return None
        runner = runner.get_next()

    while runner:
        current = current.get_next()
        runner = runner.get_next()

    return current.get_data()


ll = LinkedList()
ll.generate(5, 0, 9)
ll.print_list()
