# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

import functools


class log(object):

    def __init__(self, func):
        print "__init__"

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        self.func = wrapper

    def __call__(self):
        self.func()


@log
def now():
    print '2015-08-05'

now()

print dir(now)
