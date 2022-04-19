import unittest
from solution import check_all_same_char

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
    
    def test_check_all_same_char_2(self):
        input_str = 'aa'
        output = check_all_same_char(input_str)
        self.assertTrue(output)
    
    def test_check_all_same_char_5(self):
        input_str = 'qqqqq'
        output = check_all_same_char(input_str)
        self.assertTrue(output)
