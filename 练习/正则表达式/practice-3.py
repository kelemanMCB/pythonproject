# 拆分长字符串

import re

def chaifen():
    poem = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"
    sentence_list = re.split('[，。，。]', poem)
    for i in sentence_list:
        print(i)

if __name__ == '__main__':
    chaifen()