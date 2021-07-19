"""
Task: Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
import unittest


def unique(string):
    """
    Algorithm to determine if a string's characters are all unique
    :param string: input string (ASCII character set)
    :return: Boolean
    """
    # Special Case, cannot be greater than 128 characters
    if len(string) > 128:
        return False

    # Set up "Empty" list for observed characters
    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)  # ord converts a character to its unicode value
        if char_set[val]:  # char has already been observed
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = ['abcd', 's4fad', '']
    dataF = ['23ds2', 'hb 627jh=j ()']

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
