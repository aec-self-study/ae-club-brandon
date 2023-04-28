# tests/test_subtract.py
import unittest
from calc import aec_divide
 
class TestSubtract(unittest.TestCase):
 
    def test_divide(self):
        arg_ints = [20, 5]
        divide_result = aec_divide(arg_ints)
        self.assertEqual(divide_result, 4)

    def test_cant_divide_by_zero(self):
        arg_ints = [5, 0]
        divide_result = aec_divide(arg_ints)
        self.assertEqual(divide_result, 0)

    def test_two_args_only(self):
        arg_ints = [20, 4, 5]
        with self.assertRaises(Exception):
            aec_divide(arg_ints)
 
if __name__ == '__main__':
    unittest.main()