# 练习1：实现计算求最大公约数和最小公倍数的函数。

# 最大公约数
def gys(x, y):
    # 先把2个数从小到大排列
    if x > y:
        x, y = y, x

    # 求最大公约数
    for yinzi in range(x, 0, -1):
        if x % yinzi == 0 and y % yinzi == 0:
            return(yinzi)

