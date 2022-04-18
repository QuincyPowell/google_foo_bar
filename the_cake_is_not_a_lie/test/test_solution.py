import unittest
from the-cake-is-not-a-lie.solution import solution

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
        input = 'abcabcabcabc'
        expected_output = 4
        output = solution(input)
        self.assertEqual(expected_output, output)
    
    def test_google_test_case2(self):
        input = 'abccbaabccba'
        expected_output = 2
        output = solution(input)
        self.assertEqual(expected_output, output)
    
    def test_all_same_letter(self):
        input = 'aaaaa'
        expected_output = 5
        output = solution(input)
        self.assertEqual(expected_output, output)
    
    def test_one_character(self):
        input = 'a'
        expected_output = 1
        output = solution(input)
        self.assertEqual(expected_output, output)
    
    # This scenario is considered out of schope
    def test_empty(self):
        input = ''
        expected_output = 0
        output = solution(input)
        self.assertEqual(expected_output, output)
