# All Rights Reserved, Copyright (c) FUJITSU LIMITED 2015
# Author: luzhiyuan
# Created on: 2015/08/08

from contextlib import contextmanager


class NotFound(Exception):
    status_code = 404
    message = "Not found"


@contextmanager
def SessionConnection():
    session = "connection"
    print '[Allocate resources]'
    print 'Code before yield-statement executes in __enter__'
    yield session
    print 'Code after yield-statement executes in __exit__'
    print '[Free resources]'


def raise_exc1():
    with SessionConnection() as session:
        print session
        # raise NotFound("raise_exc1")

print '#' * 50
raise_exc1()


def raise_exc2():
    try:
        raise NotFound("raise_exc2")
    except Exception as e:
        print e
        print e.__class__
    else:
        pass
    finally:
        pass

print '#' * 50
raise_exc2()
