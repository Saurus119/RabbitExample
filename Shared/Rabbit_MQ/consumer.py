class DemoConsumer:
    def __init__(self, queue_name: str = None) -> None:
        self.queue_name = queue_name

    async def consume(self, message):
        async with message.process():
            print("Message processing by simple worker")
            print(message.body.decode("utf-8"))


# may spawn through asyncio and run multiple workes at the same time.
async def worker(message):
    async with message.iterator() as queue_iter:
        async for message in queue_iter:
            print("Processing" + message.body.decode("utf-8"))