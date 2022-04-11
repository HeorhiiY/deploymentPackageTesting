import unittest
import numpy as np
from mymodule.functions import say_hi, make_np_array
class TestFunction(unittest.TestCase):
    def test_say_hi(self):
        name = 'Brandon'
        expected_result = 'Hi, Brandon!'
        self.assertEqual(expected_result, say_hi(name))

    def test_make_np_array(self):
        ar = [3,3,3]
        expected_result = np.array(ar)
        self.assertTrue(np.alltrue(expected_result == make_np_array(ar)))


