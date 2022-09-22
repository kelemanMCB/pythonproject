# 练习1：输入一个正整数判断是不是素数。

# 调用平方根包
from math import sqrt

num = int(input("输入一个正整数:"))
end = int(sqrt(num))
# 没有被其他数整除的标记
is_prime = True
# 判断这个正整数是否能被其他数整除
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False  # 变量值变为False，说明被其他数整除了
        break

if is_prime and num != 1:
    print("素数")
else:
    print("非素数")
