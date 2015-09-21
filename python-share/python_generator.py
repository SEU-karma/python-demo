# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

def gen():
    print "start"
    n = yield 1
    print "gen: n = ", n
    n = yield 2
    print "gen: n = ", n
    n = yield 3
    print "gen: n = ", n
    n = yield 4
    print "gen: n = ", n
    print "end"

x = gen()
print x.next()
print x.next()
print x.next()
print x.next()

y = gen()
print '#' * 50
print y.send(None)
print y.send(10)
print y.send(11)
print y.send(12)

z = gen()
print '#' * 50
print z.next()
print z.next()
print z.close()
print z.next()