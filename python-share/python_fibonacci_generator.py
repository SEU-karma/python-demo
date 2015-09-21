# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1

f = fib(6)

print next(f)
print next(f)
print next(f)
print f.next()
print next(f)
print next(f)


print '#' * 50
for n in fib(6):
    print(n)
