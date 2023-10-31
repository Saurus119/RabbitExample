from contextlib import asynccontextmanager

from Shared.Rabbit_MQ.config import MessageExchangeClient
from Shared.Rabbit_MQ.consumer import DemoConsumer
from Shared.Rabbit_MQ.Enums.que import QueEnum

@asynccontextmanager
async def lifespan(app):
    client = MessageExchangeClient(QueEnum.TEST_QUEUE.value)
    if not client.is_connected:
        await client.intiialize()
    consumer = DemoConsumer(client.queue)
    await client.queue.consume(consumer.consume)
    yield