import unittest

class TestISBNVerifier(unittest.TestCase):
    def test_valid_isbn(self):
        self.assertTrue(is_valid_isbn("978-3-16-148410-0"))

    def test_invalid_isbn(self):
        self.assertFalse(is_valid_isbn("123-4-56-789012-3"))

if __name__ == '__main__':
    unittest.main()