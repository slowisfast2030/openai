# 定义一个简单的类
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


# 编写单元测试
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行前都会执行该方法
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 3), -1)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertRaises(ValueError, self.calculator.divide, 4, 0)
        self.assertAlmostEqual(self.calculator.divide(5, 3), 1.6666666666666667, delta=0.00001)


if __name__ == '__main__':
    unittest.main()