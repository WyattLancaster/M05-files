# m05 - Programming Assignment - Testing
# author: WJL
# created: 2022-02-19
# program uses unittest to test code for errors and defines 'test_sum' that tests the sum of the dictionary 1, 2, and 3 == 6 or "Should be six" if false then does the same thing only in tuple form


# import unittest
import unittest

# defines the class TestSum using TestCase from unittest
class TestSum(unittest.TestCase):

    # def test_sum
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # define test_sum_tuple
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# test if everything passed properly and print if it did
if __name__ == '__main__':
    unittest.main()