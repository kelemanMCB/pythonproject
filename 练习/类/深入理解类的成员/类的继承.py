"""
继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍
生类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发
中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。下面
我们先看一个继承的例子。
"""

"""父类"""
class Person(object):
    """构造函数"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_tv(self):
        if self._age < 18:
            print("%s只能看熊出没" % self._name)
        else:
            print("%s正在看爱情动作片" % self._name)

"""一个子类"""
class Student(Person):

    """子类的构造方法"""
    def __init__(self, name, age, grade):
        """继承父类的属性"""
        super(Student, self).__init__(name, age)
        """子类新增的属性"""
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):  # 变量 course 通过外部传入
        print("%s的%s正在学习%s" % (self._grade, self._name, course))

"""另一个子类"""
class Teacher(Person):

    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s正在讲解%s" % (self._name, self._title, course))


def main():
    stu = Student("marbem", 20, "初三")
    stu.study("Python")
    stu.watch_tv()

    tea = Teacher("Mr.zhang", 29, "艺术家")
    tea.teach("漫画")
    tea.watch_tv()

if __name__ == "__main__":
    main()











