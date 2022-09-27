# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
# 通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
# 不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

from abc import ABCMeta, abstractmethod

"""
通过abc模块的ABCMeta元类和abstractmethod修饰器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
"""
class Pets(object, metaclass=ABCMeta):

    def __init__(self, pet_name):
        self._pet_name = pet_name

    """抽象方法"""
    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pets):

    def make_voice(self):
        print("%s: wang wang wang" % self._pet_name)

class Cat(Pets):

    def make_voice(self):
        print("%s: miao miao miao" % self._pet_name)

def main():
    pets = [Dog("huang"), Cat("hong"), Dog("lan")]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()
