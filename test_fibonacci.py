import unittest

from Fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_Fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)


if __name__ == "__main__":
    unittest.main()