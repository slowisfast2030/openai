# 定义Student类
class Student:
    # 初始化方法，接受name和age两个参数
    def __init__(self, name, age):
        # 将参数赋值给实例属性
        self.name = name
        self.age = age

    # 定义greet方法，返回一个问候语
    def greet(self):
        return f"Hello, I am {self.name}, and I am {self.age} years old."