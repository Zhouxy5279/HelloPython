# -*- coding: utf-8 -*-

# Author      - Zhou-xy
# Email       - zhouxy5279@foxmail.com/1145733074@qq.com
# Time        - 2021/11/24


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


class Son(Father, Mother):

    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        super(Son, self).__init__(*args)  # Son -> Father -> Mother -> Grandpa


Son(1, ab=1)

