import unittest
from solution import eliminate_div_and_multiples

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
    
    def test_eliminate_div_and_multiples_simplified2(self):
        input_div = 2
        input_possible_divs = list(range(2, 10))
        expected = list(range(3, 10, 2))
        eliminate_div_and_multiples(input_div, input_possible_divs)
        self.assertEqual(expected, input_possible_divs)
