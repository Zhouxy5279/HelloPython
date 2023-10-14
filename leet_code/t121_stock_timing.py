# -*- coding: utf-8 -*-

# 121. 买卖股票的最佳时机
# 简单

# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

import random

prices = [random.randint(1, 15) for i in range(4, 10)]

print(prices)
min_p = prices[0]
max_profit = 0
last = prices[0]
zero_flag = True  # 赚不到
for i in range(len(prices)):
    dp = prices[i] - last
    if dp > 0:
        zero_flag = False  # 只要有一天涨就赚得到钱
        max_profit = max(max_profit, prices[i] - min_p)
    if prices[i] < min_p:
        min_p = prices[i]
    last = prices[i]

print(max_profit)

# 优化后

min_p = prices[0]
max_profit = 0
last = prices[0]
for i in range(len(prices)):
    dp = prices[i] - last
    if dp > 0:
        max_profit = max(max_profit, prices[i] - min_p)
    if prices[i] < min_p:
        min_p = prices[i]
    last = prices[i]


