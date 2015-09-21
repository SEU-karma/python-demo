# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print a
        a, b = b, a + b
        n = n + 1

fib(6)