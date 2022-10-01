# 例子3：替换字符串中的不良内容

import re

def buliang():
    sentence = '你真是个SB，我操你大爷的，fuck you'
    purified = re.sub('[SB]|[操艹日]|fuck', '*', sentence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    buliang()