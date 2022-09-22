heardMum = 2

if int(input("请输入第一次猜想的数字：")) == heardMum:
    print("真厉害，第一次就猜对了！")
elif int(input("猜错了，再猜一次：")) == heardMum:
    print("猜对了！")
elif int(input("猜错了，再最后猜一次：")) == heardMum:
    print("猜对了！")
else:
    print("三次机会用完了哦，真笨！")