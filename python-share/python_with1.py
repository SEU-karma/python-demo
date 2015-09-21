class NotFound(Exception):
    status_code = 404
    message = "Not found"


class SessionConnection(object):

    def __init__(self):
        print '__init__'
        self.session = None

    def __enter__(self):
        print '__enter__'
        self.session = "connection"
        return self.session

    def __exit__(self, exception_type, exception_value, exception_traceback):
        print '__exit__'
        print exception_type
        print exception_value
        print exception_value.__class__
        return True


def raise_exc1():
    with SessionConnection() as session:
        print session
        raise NotFound("raise_exc1")

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
