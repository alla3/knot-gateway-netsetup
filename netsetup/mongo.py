from pymongo import MongoClient

#client = MongoClient('mongodb://localhost:27017/')

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

    def drop_db(self, database): #client.knot_fog client.knot_web
        try:
            self.client.drop_database(database)
        except Exception as error:
            raise error

    def drop_all(self):
        for db in self.client:
            self.drop_db(db)
