
class ConsumerRegistry:
    consumers = {}

    @staticmethod
    def append(cls):
        ConsumerRegistry.consumers[str(cls)] = cls


class Consumer:
    def __init__(self, exchange):
        ConsumerRegistry.append(exchange)

