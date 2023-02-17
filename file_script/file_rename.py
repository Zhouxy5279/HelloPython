# -*- coding: utf-8 -*-

# Author      - Zhou-xy
# Email       - zhouxy5279@foxmail.com/1145733074@qq.com
# Time        - 2022/3/9

"""
文件重命名-替换
"""

import os


file_list = os.listdir()
print(file_list)
for i in file_list:
    os.rename(i, i.replace('block', 'corner', 1))
