import unittest
from unittest.mock import patch
from io import StringIO
import mastermind

class function_test(unittest.TestCase):
    def test_return_value(self):
        result = mastermind.create_code()
        for item in result:
            self.assertGreaterEqual(item,1)
            self.assertLessEqual(item,8)
        self.assertEqual(len(result),4)
    
    def test_correctness(self):
        result = mastermind.check_correctness(4,1) 
        self.assertTrue(result)
    
    @patch("sys.stdin",StringIO('123\n1234\n12345\n'))
    def test_input(self):
        result = mastermind.get_user_code()
        self.assertEqual(result,'1234')

if __name__ == "__main__":
    unittest.main()
