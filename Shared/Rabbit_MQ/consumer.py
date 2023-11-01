class DemoConsumer:
    def __init__(self, queue_name: str = None) -> None:
        self.queue_name = queue_name

    async def consume(self, message):
        async with message.process():
            print("Message processing by simple worker")
            print(message.body.decode("utf-8"))
