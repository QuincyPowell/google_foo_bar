import unittest
from solution import check_div1

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
    
    def test_check_div1_2(self):
        input_str = 'aa'
        output = check_div1(input_str)
        self.assertTrue(output)
    
    def test_check_div1_5(self):
        input_str = 'qqqqq'
        output = check_div1(input_str)
        self.assertTrue(output)
