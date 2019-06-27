from pika import BlockingConnection
from pika import ConnectionParameters

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

class RabbitMQConn(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.params = ConnectionParameters()

    def connect(self):
        self.conn = BlockingConnection(parameters=self.params)
        #self.conn = BlockingConnection()
        self.ch = self.conn.channel()

    def remove_queue(self, queue_name): # knot-fog-message knot-cloud-message
        self.ch.queue_purge(queue=queue_name)
        self.ch.queue_delete(queue=queue_name)

    def remove_all(self):
        queues = ['knot-fog-message', 'knot-cloud-message', 'knot-control-message']
        for queue in queues:
            self.remove_queue(queue)

    def close(self):
        self.ch.close()
        self.conn.close()
