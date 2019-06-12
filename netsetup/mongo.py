from pymongo import MongoClient

#client = MongoClient('mongodb://localhost:27017/')

#client.knot_fog
#client.knot_web

class MongoConn():

    def __init__(self, host, port = None):
        try:
            self.client = MongoClient(host, port)
        except Exception as error:
            raise error

    def drop_db(self, database):
        try:
            self.client.drop_database(database)
        except Exception as error:
            raise error

    def drop_all_db(self):
        for db in self.client:
            self.drop_db(db)
