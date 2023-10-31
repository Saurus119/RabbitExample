import asyncio
from aio_pika import connect, Message

async def worker(queue_name):
    connection = await connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue(queue_name)

    consumer = DemoConsumer(queue_name)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            await consumer.consumer(message)