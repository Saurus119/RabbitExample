from Shared.Rabbit_MQ.config import MessageExchangeClient
from Shared.Rabbit_MQ.Enums.que import QueEnum
from aio_pika import Message

class RabbitTestController:

    def __init__(self, message_client = MessageExchangeClient):
        self.message_client = message_client(QueEnum.TEST_QUEUE.value)

    async def get(self):
        print(self.message_client.is_connected)
        if not self.message_client.is_connected:
            await self.message_client.intiialize()

        # Publish a message to the queue
        messages = [Message(f"Hello, RabbitMQ! : {i}".encode()) for i in range(1000)]
        await self.message_client.send_batch_message(messages)
        return "Message added"
        