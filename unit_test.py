import unittest

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2+2, 4)
        
    def test_subtraction(self):
        self.assertEqual(5-3, 2)
        
    def test_multiplication(self): # renamed from 'test_multiply'
        self.assertEqual(multiply(3, 4), 12)
        
    def test_negative_multiplication(self):
        self.assertEqual(multiply(-3, 4), -12)
        
if __name__ == '__main__':
    unittest.main()

