import unittest
from solution import check_div

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
    
    def test_check_div_bad_remainder(self):
        input_str = 'qweewqq'
        div_count = 3
        output = check_div(div_count, input_str)
        self.assertFalse(output)
    
    def test_check_div_bad_string(self):
        input_str = 'qweewq'
        div_count = 3
        output = check_div(div_count, input_str)
        self.assertFalse(output)
        
    def test_check_div_good_input_divisions2(self):
        input_str = 'abcabc'
        div_count = 2
        output = check_div(div_count, input_str)
        self.assertTrue(output)
        
    def test_check_div_good_input_divisions3(self):
        input_str = 'abcabcabc'
        div_count = 3
        output = check_div(div_count, input_str)
        self.assertTrue(output)
