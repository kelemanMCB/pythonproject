# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。

# 获取三条边长
a = float(input("请输入第一条边长："))
b = float(input("请输入第二条边长："))
c = float(input("请输入第三条边长："))

# 判断是否能构成三角形
bj = True
if a + b > c and a + c > b and b + c > a:
    bj
    p = (a + b + c)/2
    size = (p*(p-a)*(p-b)*(p-c))**0.5
    print("所构成三角形的边长为：%.2f,面积为：%.2f" % (a + b + c,size))
else:
    bj = False
    print("三条边无法构成三角形")
