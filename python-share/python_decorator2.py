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
