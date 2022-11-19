# coding: utf-8

import unittest
from algorithms.example.sum import my_sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6)
