"""
定义一个“动物”基类，包含一个“叫”的方法（默认输出“某种动物在叫”）。
- 定义“狗”和“猫”两个子类，重写“叫”方法以输出特定的叫声。
- 创建“狗”和“猫”对象，并调用“叫”方法。
"""


# 动物基类
class Animal:
    def make_sound(self):
        print("某种动物在叫")  # 方法


class Dog(Animal):
    def make_sound(self):
        print("汪汪汪！")


class Cat(Animal):
    def make_sound(self):
        print("喵喵喵喵喵喵喵~~~")


# 创建对象并调用方法
if __name__ == "__main__":
    dog = Dog()
    print("狗叫:")
    dog.make_sound()

    cat = Cat()
    print("猫叫:")
    cat.make_sound()

