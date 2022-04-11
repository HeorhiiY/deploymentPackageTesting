import unittest
import numpy as np
from mymodule.functions import say_hi
class TestFunction(unittest.TestCase):
    def test_say_hi(self):
        name = 'Brandon'
        expected_result = 'Hi, Brandon!'
        self.assertEqual(expected_result, say_hi(name))


