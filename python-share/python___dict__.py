# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# a demo to show fields in class or instance
# Created on: 2015/08/08

"""
two methods to show fields
"""

class Fruit(object):

    '''
    Fruit class.
    '''

    __a = 1
    b = 2

    def __init__(self):
        self.__color = "red"
        self.__price = 10
        self.price = 11


class Apple(Fruit):
    __c = 3
    d = 4

if __name__ == "__main__":
    fruit = Fruit()
    apple = Apple()

    print Fruit.__dict__
    print fruit.__dict__
    print Apple.__dict__
    print apple.__dict__

    print '#' * 50
    print dir(Fruit)
    print dir(fruit)
    print dir(Apple)
    print dir(apple)
