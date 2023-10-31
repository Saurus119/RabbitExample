from typing import List
import asyncio

from aio_pika import connect, Message, Exchange
from Shared.Rabbit_MQ.consumer import DemoConsumer
from Shared.Rabbit_MQ.Enums.routing_keys import RoutingKey

class RabbitConnection:
    STRING = "amqp://guest:guest@localhost/"

class MessageExchangeClient:
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.is_connected = False
        self.channel = None
        self.connection = None
        self.queue = None

    async def intiialize(self):
        if not self.is_connected:
            await self.connect()
            await self.create_channel_and_que()

    async def connect(self) -> None:
        try:
            self.connection = await connect(RabbitConnection.STRING)
            self.is_connected = True
            self.channel = None
        except Exception:
            self.is_connected = False

    async def create_channel_and_que(self) -> None:
        self.channel = await self.connection.channel()
        self.queue = await self.channel.declare_queue(self.queue_name)
        self.exchange = Exchange(self.channel, 'test_abc', type='direct')
        await self.exchange.declare()
        # Bind the queue to the exchange (you can adjust the routing key as needed)
        await self.queue.bind(self.exchange, routing_key=RoutingKey.TEST_ROUTE.value)

    async def send_message(self,  message: Message):
        await self.exchange.publish(message, routing_key=RoutingKey.TEST_ROUTE.value)

    async def send_batch_message(self, messages: List[Message]) -> None:
        send_coroutines = [self.send_message(message) for message in messages]
        await asyncio.gather(*send_coroutines)
