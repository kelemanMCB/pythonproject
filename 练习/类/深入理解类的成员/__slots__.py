"""
__slots__魔法
我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的
属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通
过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象
生效，对子类并不起任何作用。
"""




class People(object):
    """限定People对象只能绑定_name, _age, _gender 这三个属性"""
    __slots__ = ("_name", "_age", "_gender")

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

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋。" % self._name)
        else:
            print("%s正在玩斗地主。" % self._name)

def main():
    p = People("marbem", 22)
    p.play()
    # p._gender = "男"

if __name__ == "__main__":
    main()