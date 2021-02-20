import unittest


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_maksym_orzhahivsky_fi_93(self):
        self.assertEqual(sum([1,2,3])/len([1,2,3]), 2)


if __name__ == '__main__':
    unittest.main()
