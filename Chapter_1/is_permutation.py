"""
Task: Check Permutation
Given two strings, write a method to decide if one is a permutation of the other
"""

import unittest


def check_permutation(string1, string2):
    """
    Algorithm to determine if two strings are permutations of the other
    :param string1: String
    :param string2: String
    :return: Boolean
    """

    def make_dictionary(string):
        """
        Helper function to make a dictionary mapping characters to observations
        :param string: input string
        :return: dictionary mapping characters to observations
        """
        dict_ = {}
        for char in string:
            if char in dict_.keys():
                dict_[char] += 1
            else:
                dict_[char] = 1
        return dict_

    # Special Cases, can't be permutations if different lengths or empty
    if len(string1) != len(string2):
        return False

    if string1 is None or string2 is None:
        return False

    string1_dict = make_dictionary(string1)
    string2_dict = make_dictionary(string2)

    for key, value in string1_dict.items():
        if key not in string2_dict.keys():
            return False
        if string2_dict[key] != value:
            return False

    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
