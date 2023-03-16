import unittest

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        # Test addition of two positive integers
        self.assertEqual(2 + 2, 4)
        
    def test_subtraction(self):
        # Test subtraction of two positive integers
        self.assertEqual(5 - 3, 2)
        
    def test_multiplication(self):
        # Test multiplication of two positive integers
        self.assertEqual(multiply(3, 4), 12)
        
    def test_negative_multiplication(self):
        # Test multiplication of a negative and positive integer
        self.assertEqual(multiply(-3, 4), -12)
        
if __name__ == '__main__':
    unittest.main()
