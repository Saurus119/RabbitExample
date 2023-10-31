import json
from Pika import BasicProperties
from Shared.Rabbit_MQ.config import PikaConfig

class PikaClient(PikaConfig):

    def __init__(self, process_callback):
        super().__init__(process_callback)

    async def consume(self, loop):
        pass

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        message.ack()
        body = message.body
        print('Received message')
        if body:
            self.process_callable(json.loads(body))

    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )

