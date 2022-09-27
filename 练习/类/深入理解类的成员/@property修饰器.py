# @property 修饰器
# 提供getter和setter方法

class people(object):
    """构造函数"""
    def __init__(self, name, age):
        """实例变量前加 “_” """
        self._name = name
        self._age = age

    """修饰器"""
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    """一个方法"""
    def play(self):
        if self._age < 18:
            print("你的年龄是：%d，不能玩这么危险的游戏。" % self._age)
        else:
            print("你的年龄是：%d，可以玩这么危险的游戏。" % self._age)

def main():
    p = people("marbem", 16)
    p.play()
    p.age = 22
    p.play()

"""执行"""
if __name__ == "__main__":
    main()