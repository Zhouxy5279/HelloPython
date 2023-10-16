# -*- coding: utf-8 -*-

# 260. 只出现一次的数字 III
# 中等

# 给你一个整数数组 nums ，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

import random

ri = random.randint(4, 10)
example = []
for i in range(ri-1):
    example += [i] * 2
example += [ri-1, ri-2]
random.shuffle(example)
print(example)

test_items = (len(example) + 1) / 3
single_n = []
multi_n = []
for e in example:
    if e in single_n:
        single_n.remove(e)
        multi_n.append(e)
    elif e not in multi_n:
        single_n.append(e)

    if len(multi_n) == test_items - 2 and len(single_n) == 2:
        print(single_n)
        break










