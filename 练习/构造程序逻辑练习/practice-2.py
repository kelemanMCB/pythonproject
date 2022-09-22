# 正整数的反转

# 输入一个正整数
num = int(input("请输入一个正整数："))
# 初始化反转数
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

