from pika import BlockingConnection
from pika import ConnectionParameters

class RabbitMQConn():

    def __init__(self):
        self.params = ConnectionParameters()

    def connect(self):
        self.conn = BlockingConnection(parameters=self.params)
        #self.conn = BlockingConnection()
        self.ch = self.conn.channel()

    def removeQueue(self, queue_name): # knot-fog-message knot-cloud-message
        self.ch.queue_purge(queue=queue_name)
        self.ch.queue_delete(queue=queue_name)

    def close(self):
        self.ch.close()
        self.conn.close()
