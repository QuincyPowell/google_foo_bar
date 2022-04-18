import unittest
from solution import solution

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
    
    def test_google_test_case1(self):
        input_str = 'abcabcabcabc'
        expected_output = 4
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_google_test_case2(self):
        input_str = 'abccbaabccba'
        expected_output = 2
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_all_same_letter(self):
        input_str = 'aaaaa'
        expected_output = 5
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_one_character(self):
        input_str = 'a'
        expected_output = 1
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    # This scenario is considered out of schope
    def test_empty(self):
        input_str = ''
        expected_output = 0
        output = solution(input_str)
        self.assertEqual(expected_output, output)
