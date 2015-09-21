from python_sqlalchemy import UserORM


def add_user(name):
    kwargs = {
        'name': name,
        'password': 'luzy',
        'description': 'luzhiyuan'
    }
    UserORM.add_user(kwargs)


def get_user(name):
    print UserORM.get_user(name)


def update_user(name):
    kwargs = {
        'name': 'luzy',
        'password': 'luzy',
        'description': 'FNST'
    }
    UserORM.update_user(name, kwargs)


def delete_user(name):
    UserORM.delete_user(name)

# add_user('luzy')
# add_user('ssss')
# get_user('luzy')
# delete_user('luzy')
update_user('ssss')
