from pika import BlockingConnection
from pika import ConnectionParameters
from pika import exceptions

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

class RabbitMQConn(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.params = ConnectionParameters()

    def connect(self):
        try:
            self.conn = BlockingConnection(parameters=self.params)
            self.ch = self.conn.channel()
        except Exception as error:
            raise error

    def remove_queue(self, queue_name):
        try:
            logging.info('Removing queue: ' + queue_name)
            self.ch.queue_purge(queue=queue_name)
            self.ch.queue_delete(queue=queue_name)
        except (exceptions.ChannelWrongStateError,
                exceptions.ChannelClosed) as error:
            logging.error('Error: ' + str(error))

    def remove_all(self):
        queues = ['knot-fog-message', 'knot-cloud-message', 'knot-control-message']
        for queue in queues:
            self.remove_queue(queue)

    def close(self):
        self.ch.close()
        self.conn.close()
