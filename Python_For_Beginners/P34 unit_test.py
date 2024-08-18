# Owner: Ryan
# Date: 11-Aug-2024

import unittest
from P34_my_calculator import my_adder


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5, 3), 8)

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)
