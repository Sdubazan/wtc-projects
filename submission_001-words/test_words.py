import unittest
import sys
import word_processor


class My_functions_Test(unittest.TestCase):
    def test_step1_convert_word_list_1(self):
        results = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        expected = ['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you']
        self.assertEqual(results,expected)

    def test_empty_word_list(self):
        results = word_processor.convert_to_word_list('')
        expected = []
        self.assertEqual(results,expected)


    def test_filter_words(self):
        results = word_processor.words_longer_than(10,'These are indeed interesting, an obvious understatement, times. What say you?')
        expected = ['interesting', 'understatement']
        self.assertEqual(results,expected)

    def test_word_lengths(self):
        results = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        expected = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(results,expected)

    def test_empty_word_lengths(self):
        results = word_processor.words_lengths_map('')
        expected ={}
        self.assertEqual(results,expected)

    def test_letters_count(self):
        results = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        expected = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(results,expected)

    def test_letters_count_empty(self):
        results = word_processor.letters_count_map('')
        expected = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertEqual(results,expected)

    def test_1_char_most_used(self):
        results = word_processor.most_used_character('a')
        expected = 'a'
        self.assertEqual(results,expected)

    def test_most_used(self):
        results = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        expected = 'e'
        self.assertEqual(results,expected)

    def test_most_used_empty(self):
        results = word_processor.most_used_character('')
        self.assertIsNone(results)

if __name__ == "__main__":
    unittest.main()