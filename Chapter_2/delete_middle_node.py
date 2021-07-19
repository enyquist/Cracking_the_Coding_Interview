"""
Task: Delete Middle Node
Implement an algorithm to delete a node in the middle (i.e. any node but
the first and last node) of a singly linked list, given only access to that node
"""

from CtCI_custom_classes.linked_list import LinkedList, Node


def delete_node(node):
    node.set_data(node.get_next().get_data())
    node.set_next(node.get_next().get_next())


ll = LinkedList()
ll.generate(3, 0, 9)
ll.print_list()

middle_node = ll.insert(5)
ll.print_list()

ll.generate(3, 0, 9)
ll.print_list()

delete_node(Node(4))
ll.print_list()
