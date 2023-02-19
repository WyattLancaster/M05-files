# m05 - Programming Assignment - Testing
# author: WJL
# created: 2022-02-19
# program uses unittest to test code for errors and defines 'test_sum' that tests the sum of the dictionary 1, 2, and 3 == 6 or "Should be six" if false then does the same thing only in tuple form

# import unittest
import unittest

# import my_sum and fractions
from my_sum import sum
from fractions import Fraction

# defines the class TestSum using TestCase from unittest as well as a fraction test
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

# test if everything passed properly
if __name__ == '__main__':
    unittest.main()