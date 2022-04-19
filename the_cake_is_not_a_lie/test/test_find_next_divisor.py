import unittest
from solution import find_next_divisor

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_find_next_divisor_bad_remainder(self):
        input_str = 'qweewqq'
        expected_output = None
        output = find_next_divisor(input_str)
        self.assertEqual(expected_output, output)
    
    def test_find_next_divisor_bad_string(self):
        input_str = 'qwertyzx'
        expected_output = None
        output = find_next_divisor(input_str)
        self.assertEqual(expected_output, output)
        
    def test_find_next_divisor_good_input_divisions2(self):
        input_str = 'abcabc'
        expected_output = 2
        output = find_next_divisor(input_str)
        self.assertEqual(expected_output, output)
        
    def test_find_next_divisor_good_input_divisions3(self):
        input_str = 'abcabcabc'
        expected_output = 3
        output = find_next_divisor(input_str)
        self.assertEqual(expected_output, output)
