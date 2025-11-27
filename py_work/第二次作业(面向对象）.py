# 定义一个“学生”类，包含姓名、年龄和成绩属性，以及一个计算平均成绩的方法。
# 创建几个“学生”对象，并调用方法计算并打印他们的平均成绩。
class Student:
    def __init__(self, student_id, name, age, **scores):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.scores = scores

    def average_grade(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def report(self):
        avg = self.average_grade()
        print(f"学号:{self.student_id}, 姓名:{self.name}, 年龄:{self.age}")
        print("各科成绩:")
        for subject, score in self.scores.items():
            print(f"  {subject}: {score}")
        print(f"平均成绩: {avg:.2f}")


# 创建学生对象
students = [
    Student("20250511", '老登', 54, math=99, English=88, Chinese=97),
    Student("20250512", '小登', 19, math=76, English=88, Chinese=95),
    Student("20250513", 'maomao', 20, math=90, English=85, Chinese=92)
]

# 输入学号并查找学生
student_id_put = input("请输入学号: ")
found = False

for student in students:
    if student.student_id == student_id_put:
        student.report()
        found = True
        break

# 这个判断应该在for循环外部
if not found:
    print("未找到该学号的学生")
