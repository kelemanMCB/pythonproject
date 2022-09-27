# 描述数字时钟的类

import os
from time import sleep


class Clock(object):
    """构造函数"""
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute =  minute
        self.second = second

    """时间运行"""
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    """显示时间"""
    def show(self):
        return f"{self.hour}:{self.minute}:{self.second}"


"""执行函数"""
if __name__ == "__main__":
    c = Clock(23, 59, 59)
    while True:
        print(c.show())
        sleep(1)
        c.run()
        os.system('cls')  # 清屏
        

