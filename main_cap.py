import unittest
import cap_fun


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap_fun.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_words(self):
        text = 'a book'
        result = cap_fun.cap_text(text)
        self.assertEqual(result, 'A Book')


if __name__ == '__main__':
    unittest.main()
