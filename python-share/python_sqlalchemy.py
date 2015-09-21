from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


_ENGINE = None
DBBase = declarative_base()


# engine


def get_engine():

    kwargs = {
        'drivername': 'mysql',
        'username': 'luzy',
        'password': 'luzy_pass',
        'host': 'localhost',
        'database': 'horizon',
        'query': {'charset': 'utf8'}
    }

    engine_url = URL(**kwargs)

    global _ENGINE
    if _ENGINE is None:
        _ENGINE = create_engine(engine_url)
    return _ENGINE


# table
def create_tables():
    DBBase.metadata.create_all(get_engine())


class User(DBBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255))
    description = Column(Text)

    def __init__(self, id=None, name=None, password=None, description=None):
        self.id = id
        self.name = name
        self.password = password
        self.description = description

    def __repr__(self):
        str = "id='%s', password='%s', name='%s', description='%s'"
        info = "<%s(%s)>" % ('User', str)
        return info % (self.id, self.password, self.name, self.description)

create_tables()


# session
DBSession = scoped_session(sessionmaker(bind=get_engine()))


class SessionConnection(object):

    '''
    SessionConnection object that can open and close connection context.
    '''

    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = DBSession()
        return self.session

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.session.close()
        return True

# ORM


class UserORM(object):

    '''
    provide CRUD for user.
    '''

    @staticmethod
    def add_user(user_info):
        user = User(**user_info)
        with SessionConnection() as session:
            session.add(user)
            session.commit()
        return user

    @staticmethod
    def get_user(name):
        with SessionConnection() as session:
            item = session.query(User).filter(
                User.name == name).first()
        return item

    @staticmethod
    def update_user(name, user_info):
        with SessionConnection() as session:
            item = session.query(User).filter(
                User.name == name).first()
            for key in user_info.keys():
                setattr(item, key, user_info[key])
            session.commit()

    @staticmethod
    def delete_user(name):
        with SessionConnection() as session:
            session.query(User).filter(User.name == name).delete()
            session.commit()
