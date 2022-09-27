# 卡牌游戏：21点

"""
定义一副牌
"""
import random


class porks(object):
    """
    初始化
    """
    def __int__(self):
        self.cards = [[face, suite] for face in "♠♣♦♥"
                      for suite in ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q"]]

    def xipai(self):
        random.shuffle(self.cards)
        return self.cards

"""
荷官
"""
# class heguan(object):
#     """
#     初始化
#     """
#     def __int__(self, cards):
#         self.cards = cards
#
#     """洗牌"""
#     def xipai(self, cards):
#         random.suffle(self.cards)

"""
执行方法
"""
if __name__ == "__main__":
    pork = porks()
    print(pork.cards)
    # for card in pork:
    #     print(card, end=" ")