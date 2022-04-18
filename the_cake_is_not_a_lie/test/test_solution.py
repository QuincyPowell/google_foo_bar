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
        
    def test_short_4_2(self):
        input_str = 'abab'
        expected_output = 2
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_short2(self):
        input_str = 'bb'
        expected_output = 2
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_long_200_2(self):
        input_str = 'eZZGzwnEQPfbfAAuEtGoEBaoshMUzSpyORSrCPruzDYHOWcuKtGTqWWakjmPmmFpBwPHxaztOcOudnpobWBvkwrxkrGvXzXpJWyKeZZGzwnEQPfbfAAuEtGoEBaoshMUzSpyORSrCPruzDYHOWcuKtGTqWWakjmPmmFpBwPHxaztOcOudnpobWBvkwrxkrGvXzXpJWyK'
        expected_output = 2
        output = solution(input_str)
        self.assertEqual(expected_output, output)
        
    def test_oversize_300_3(self):
        input_str = 'eZZGzwnEQPfbfAAuEtGoEBaoshMUzSpyORSrCPruzDYHOWcuKtGTqWWakjmPmmFpBwPHxaztOcOudnpobWBvkwrxkrGvXzXpJWyKeZZGzwnEQPfbfAAuEtGoEBaoshMUzSpyORSrCPruzDYHOWcuKtGTqWWakjmPmmFpBwPHxaztOcOudnpobWBvkwrxkrGvXzXpJWyKeZZGzwnEQPfbfAAuEtGoEBaoshMUzSpyORSrCPruzDYHOWcuKtGTqWWakjmPmmFpBwPHxaztOcOudnpobWBvkwrxkrGvXzXpJWyK'
        expected_output = 3
        output = solution(input_str)
        self.assertEqual(expected_output, output)

    # Because a periodic sequence is equal to non-trivial rotations
    # of itself we do not need to test for repition over the boundary
    
    def test_3_1(self):
        input_str = 'abc'
        expected_output = 1
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_6_2(self):
        input_str = 'abcabc'
        expected_output = 2
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_9_3(self):
        input_str = 'abcabcabc'
        expected_output = 3
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_12_4(self):
        input_str = 'abcabcabcabc'
        expected_output = 4
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_15_5(self):
        input_str = 'abcabcabcabcabc'
        expected_output = 5
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_18_6(self):
        input_str = 'abcabcabcabcabcabc'
        expected_output = 6
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_21_7(self):
        input_str = 'abcabcabcabcabcabcabc'
        expected_output = 7
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_24_8(self):
        input_str = 'abcabcabcabcabcabcabcabc'
        expected_output = 8
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_27_9(self):
        input_str = 'abcabcabcabcabcabcabcabcabc'
        expected_output = 9
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_30_10(self):
        input_str = 'abcabcabcabcabcabcabcabcabcabc'
        expected_output = 10
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_33_11(self):
        input_str = 'abcabcabcabcabcabcabcabcabcabcabc'
        expected_output = 11
        output = solution(input_str)
        self.assertEqual(expected_output, output)
    
    def test_36_12(self):
        input_str = 'abcabcabcabcabcabcabcabcabcabcabcabc'
        expected_output = 12
        output = solution(input_str)
        self.assertEqual(expected_output, output)
