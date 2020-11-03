import unittest
import super_algos

class TestFunction(unittest.TestCase):
    def test_find_min(self):
        result = super_algos.find_min([1,2,3])
        self.assertEqual(result,1)

    def test_find_sum(self):
        result = super_algos.sum_all([1,-2,3])
        self.assertEqual(result,2)

    def test_find_possible_strings(self):
        result = super_algos.find_possible_strings(['q','f'],3)
        result1 = super_algos.find_possible_strings(['a','b'],2)
        self.assertEquals(result,['fff', 'ffq', 'fqf', 'fqq', 'qff', 'qfq', 'qqf', 'qqq'])
        self.assertEquals(result1,['aa', 'ab', 'ba', 'bb'])

if __name__ == '__main__':
    unittest.main()