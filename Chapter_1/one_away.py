"""
Task: One Away
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check
if they are one edit (or zero edits) away
"""
import unittest


def one_away(s1, s2):
    """
    Check if a string can converted to another string with a single edit
    :param s1: string
    :param s2: string
    :return: Boolean
    """
    # Same Length, must be edited in place
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    # String1 is one bigger than String1, check for an insert
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    # String2 is bigger than String1, check for an insert (same as a deletion from String1)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    # Difference is greater than one
    return False


def one_edit_replace(s1, s2):
    edited = False  # Condition
    for c1, c2 in zip(s1, s2):  # Slide along each character
        if c1 != c2:  # If characters are changed
            if edited:  # If this isn't the first edit
                return False
            edited = True  # Condition change
    return True


def one_edit_insert(s1, s2):
    edited = False  # Condition
    i, j = 0, 0  # Need two pointers
    while i < len(s1) and j < len(s2):  # While there are characters
        if s1[i] != s2[j]:  # If characters are changed
            if edited:  # If this isnt the first edit
                return False
            edited = True  # Condition change
            j += 1  # Update pointer in shorter string
        else:
            i += 1  # Update Pointer
            j += 1  # Update Pointer
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
