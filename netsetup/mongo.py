from pymongo import MongoClient
from pymongo import errors

import logging

class Singleton(type):
    """
    Singleton class to guarantee that a single instance will be used for
    its inhereted classes
    """
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,
                                         cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class MongoConn(object):

    __metaclass__ = Singleton

    def __init__(self, host, port = None):
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
        except Exception as error:
            raise error

    def drop_db(self, database):
        try:
            logging.info('Removing database: ' + database)
            self.client.drop_database(database)
        except errors.ServerSelectionTimeoutError as error:
            logging.error('Fail: ' + str(error))

    def drop_all(self):
        for db in self.client.list_database_names():
            self.drop_db(db)
