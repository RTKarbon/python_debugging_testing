#!/usr/bin/env python

from program_with_bugs import *
import unittest

###############################################
# Change name of a tested function
tested_function = removeOddNumbersV3
###############################################

class RemoveOddNumberTC(unittest.TestCase):
    def test_1(self):
        even_l = tested_function([1])
        self.assertEqual(even_l, [])

    def test_2(self):
        even_l = tested_function([])
        self.assertEqual(even_l, [])

    def test_3(self):
        even_l = tested_function([2])
        self.assertEqual(even_l, [2])

    def test_4(self):
        even_l = tested_function([1, 2, 3])
        self.assertEqual(even_l, [2])

    def test_5(self):
        even_l = tested_function([1, 2, 3, 5])
        self.assertEqual(even_l, [2])

    def test_6(self):
        even_l = tested_function([1, 3, 5])
        self.assertEqual(even_l, [])


if __name__ == "__main__":
    unittest.main()