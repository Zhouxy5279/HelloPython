# -*- coding: utf-8 -*-

# Author      - Zhou-xy
# Email       - zhouxy5279@foxmail.com/1145733074@qq.com
# Time        - 2021/11/24

"""
在子类的实例化中，写在super之前的方法会优先于父类初始化方法执行
多重继承中的super会按顺序执行最后再执行更上级的父类
不同多态类中有相同方法时会以更靠前的类为准
"""


class Grandpa(object):

    def __init__(self):
        print('Grandpa_init')
        pass


class Father(Grandpa):

    def __init__(self, *args):
        print('Father_init{}'.format(args))
        super(Father, self).__init__()
        pass
    

class Mother(Grandpa):

    def __init__(self, *args):
        print('Mother_init{}'.format(args))
        super(Mother, self).__init__()


class Uncle(object):

    def __init__(self):
        print('Uncle_init')
        pass


class Annt(Uncle):

    def __init__(self, *args):
        print('Annt_init{}'.format(args))
        super(Annt, self).__init__()


class Annt2(Grandpa):

    def __init__(self, *args):
        print('Annt2_init{}'.format(args))
        super(Annt2, self).__init__()


class Son(Father, Annt2, Mother):

    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        super(Son, self).__init__(*args)  # Son -> Father -> Mother -> Grandpa


Son(1, ab=1)

