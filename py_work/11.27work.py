"""
- 在上面的“动物”类体系中，定义一个函数，接受一个“动物”对象作为参数，并调用其“叫”方法。
- 创建不同类型的“动物”对象（如“狗”、“猫”等），并将它们传递给该函数，观察多态性的表现。
"""


class Animal:
    def make_sound(self):
        print("某种动物在叫")


class Dog(Animal):
    def make_sound(self):
        print("汪汪汪汪汪汪")


class Cat(Animal):
    def make_sound(self):
        print("喵喵喵喵喵")


class Cow(Animal):
    def make_sound(self):
        print("哞~~~~牛马")


class Horse(Animal):
    def make_sound(self):
        print("马说:唐^韩愈")


class Duck(Animal):
    def make_sound(self):
        print("O! my ladyGaga")


# 定义一个函数，接受一个“动物”对象作为参数，并调用其“叫”方法。
def animal_sound(animal):
    animal.make_sound()


# 创建不同类型的“动物”对象（如“狗”、“猫”等），并将它们传递给该函数，观察多态性的表现。
if __name__ == '__main__':
    # 将对象传给函数
    dog = Dog()
    cat = Cat()
    cow = Cow()
    horse = Horse()
    duck = Duck()
    # 调用函数
    animal_sound(dog)
    animal_sound(cat)
    animal_sound(cow)
    animal_sound(horse)
    animal_sound(duck)
    # 创建列表并吧列表传给函数
    animals = [dog, cat, cow, horse, duck]
    for animal in animals:
        animal_sound(animal)
