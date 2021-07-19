"""
Task: URLify
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string
"""

import unittest


def urlify(string, length):
    """
    Algorithm to replace ' ' characters with '%20' in a string
    :param string:
    :return:
    """

    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


class Test(unittest.TestCase):
    """Test Cases"""
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
