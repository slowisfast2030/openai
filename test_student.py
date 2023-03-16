# 导入unittest模块
import unittest
# 导入被测类
from student import Student

# 定义一个继承自unittest.TestCase的测试类
class TestStudent(unittest.TestCase):
    # 定义一个以test开头的测试方法，用来测试Student类的初始化方法是否正确地赋值给实例属性
    def test_init(self):
        # 创建一个被测对象，并传入一组测试数据
        s = Student("Alice", 18)
        # 使用断言来比较实例属性和预期值是否相等
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.age, 18)

    # 定义另一个以test开头的测试方法，用来测试Student类的greet方法是否正确地返回问候语
    def test_greet(self):
        # 创建另一个被测对象，并传入另一组测试数据
        s = Student("Bob", 20)
        # 调用被测方法，并获取返回值
        result = s.greet()
        # 使用断言来比较返回值和预期值是否相等
        self.assertEqual(result, "Hello, I am Bob, and I am 20 years old.")

# 如果是直接运行这个文件，则执行以下代码
if __name__ == '__main__':
    # 调用unittest.main()方法来运行所有以test开头的测试方法，并输出结果报告
    unittest.main()
