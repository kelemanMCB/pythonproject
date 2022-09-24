# 练习1：在屏幕上显示跑马灯文字。
import os
import time


def paomadeng():

    content = "文字跑马灯还是很好看的额。。。"
    while True:
        os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == "__main__":
    paomadeng()
