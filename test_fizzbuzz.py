import unittest

from FizzBuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_Fizz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz(6), 'Fizz')
        self.assertEqual(fizz_buzz(9), 'Fizz')

    def test_Buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(20), "Buzz")

    def test_Fizz_Buzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
        self.assertEqual(fizz_buzz(45), "FizzBuzz")


    def test_print_number(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(4), 4)

if __name__ == "__main__":
    unittest.main()