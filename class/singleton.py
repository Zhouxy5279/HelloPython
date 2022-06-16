# -*- coding: utf-8 -*-

# Author      - Zhouxy5279
# Email       - zhouxy5279@qq.com
# Time        - 2022/6/16
# Description -

import weakref


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        pass


class SingletonMeta(type):
    """
    单例模式元类,将类的元类指定为本类,则该类成为单例模式
    本类会给被修改的类添加一个指向唯一对象的弱引用,因此不会干扰到Python原生的GC
    """

    def __call__(cls, *args, **kwargs):
        """元类的call方法与普通类的call方法作用不同"""
        attr_name = '__{}_SingletonMeta_ref'.format(cls.__name__)
        if not hasattr(cls, attr_name):
            instance = type.__call__(cls, *args, **kwargs)
            ref = weakref.ref(instance)
            # tip = '类 {} 没有实例,在: {} 地址创建其实例'
            setattr(cls, attr_name, ref)
        else:
            instance = getattr(cls, attr_name)()
            if instance:
                pass
                # tip = '类 {} 已经拥有实例,在: {} 地址处'
            else:
                instance = type.__call__(cls, *args, **kwargs)
                ref = weakref.ref(instance)
                # tip = '类 {} 没有实例,在: {} 地址创建其实例'
                setattr(cls, attr_name, ref)
        # print tip.format(cls.__name__, hex(id(instance)))
        return instance
