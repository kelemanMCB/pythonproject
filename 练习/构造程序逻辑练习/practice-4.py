# CRAPS赌博游戏。
#
# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。
from random import randint


# 本钱
money = 10000
while money > 0:
    isjixu = False
    print("你的总资产为：%d" % money)

# 下注
    while True:
        xiazhu = int(input("请下注："))
        if 0 < xiazhu <= money:
            print("玩家下注%d元" % xiazhu)
            break

    # 第一次摇
    first = randint(1, 6) + randint(1, 6)
    print("第一次摇，点数：%d" % first)
    if first == 7 or first == 11:
        print("玩家胜，入%d元" % xiazhu)
        money = money + xiazhu
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜，出%d元" % xiazhu)
        money = money - xiazhu
    else:
        isjixu = True
    # 第一次没有胜负，则玩家继续摇骰子
    while isjixu:
        isjixu = False
        jixuyao = randint(1, 6) + randint(1, 6)
        print("继续摇，点数：%d" % jixuyao)
        if jixuyao == 7:
            print("庄家胜，出%d元" % xiazhu)
            money = money - xiazhu
        elif jixuyao == first:
            print("玩家胜，入%d元" % xiazhu)
            money = money + xiazhu
        else:
            isjixu = True
print("你破产了，游戏结束！")