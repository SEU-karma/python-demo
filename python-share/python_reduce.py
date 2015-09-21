# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print reduce(lambda x, y: x + y, a)


def add(x, y):
    return x + y

print reduce(add, a)
