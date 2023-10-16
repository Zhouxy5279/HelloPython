# -*- coding: utf-8 -*-

# 137. 只出现一次的数字 II
# 中等

# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

import random

ri = random.randint(4, 10)
example = []
for i in range(ri):
    example += [i] * 3
example += [ri]
random.shuffle(example)
print(example)

test_items = (len(example) + 2) / 3
single_n = []
multi_n = []
for e in example:
    if e in single_n:
        single_n.remove(e)
        multi_n.append(e)
    elif e not in multi_n:
        single_n.append(e)

    if len(multi_n) == test_items - 1 and len(single_n) == 1:
        print(single_n[0])
        break










