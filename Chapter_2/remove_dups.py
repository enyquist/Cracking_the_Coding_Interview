"""
Task: Remove Dups
Write code to remove duplicates from an unsorted linked list
"""
from CtCI_custom_classes.linked_list import LinkedList


def remove_dups(ll):
    """
    Function to remove duplicates from an unsorted linked list
    :param ll: linked list object
    :return: linked list object with unique characters
    """
    # Special Cases - Empty list
    if ll.head is None:
        return

    current = ll.head
    seen = {current.get_data()}
    while current.get_next():
        if current.get_next().get_data() in seen:
            current.set_next(current.get_next().get_next())
        else:
            seen.add(current.next.get_data())
            current = current.get_next()

    return ll


def remove_dups_followup(ll):
    """
    Function to remove duplicates from an unsorted linked list without using a buffer
    :param ll: linked list object
    :return: linked list object with unique characters
    """
    # Special Cases - Empty list
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.get_next():
            if runner.get_next().get_data() == current.get_data():
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()
        current = current.get_next()

    return ll.head


ll = LinkedList()
ll.generate(10, 0, 9)
ll.print_list()
remove_dups(ll)
ll.print_list()

ll.generate(10, 0, 9)
ll.print_list()
remove_dups_followup(ll)
ll.print_list()
