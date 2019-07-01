from mongo import MongoConn
from rabbitmq import RabbitMQConn
from control import Control

class ControlFactory():
    @staticmethod
    def create(settings):
        mongodb_settings = settings.get('mongodb')
        mongo_conm = MongoConn(mongodb_settings.get('host'),
                               mongodb_settings.get('port'))
        rabbitmq_conn = RabbitMQConn()

        return Control(mongo_conm, rabbitmq_conn)
