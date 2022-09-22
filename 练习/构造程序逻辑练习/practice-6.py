# 找出10000以内的完美数。
#
# 说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
import math


for num in range(2, 10000):
    sum = 0
    for zhenyinzi in range(1, int(math.sqrt(num)) + 1):
        if num % zhenyinzi == 0:
            sum += zhenyinzi
            if zhenyinzi > 1 and num // zhenyinzi != zhenyinzi:
                sum += num // zhenyinzi
    if sum == num:
        print(sum)


