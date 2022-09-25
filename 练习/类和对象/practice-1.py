# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt

import self as self


class point(object):
    # 初始化
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 创建点
    def create_point(self, x, y):
        self.x = x
        self.y = y

    # 移动点
    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy


    # 计算两点之间的距离
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return "(%s,%s)" % (str(self.x), str(self.y))


def main():
    # 创建对象
    p1 = point(0, 0)
    p2 = point()

    print(p1)
    p2.move_to(1, 1)
    print(p2)
    print(p1.distance_to(p2))
if __name__ == "__main__":
    main()