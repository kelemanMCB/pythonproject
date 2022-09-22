# 案例需求：定义一个数字（1~10随机产生），通过3次判断来猜出数字。
# 案例要求：
#       1、数字随机产生，范围1~10；
#       2、有3次机会猜测数字，通过3层嵌套判断实现；
#       3、每次猜不中，会提示大了或小了。

import random

num = random.randint(1, 10)
aNum = int(input("您有三次机会，请输入猜的数字："))
if aNum == num:
    print("猜对了！")
else:
    if aNum > num:
        print("大了")
    else:
        print("小了")

    aNum = int(input("请再次输入数字："))
    if aNum == num:
        print("猜对了")
    else:
        if aNum > num:
            print("大了")
        else:
            print("小了")

    aNum = int(input("请最后输入数字："))
    if aNum == num:
        print("猜对了")
    else:
        print(f"错了，没机会了，正确的数字是{num}")
