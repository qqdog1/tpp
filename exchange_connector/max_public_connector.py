import abc


class MaxPublicConnector(metaclass=abc.ABCMeta):
    def subscribe(self):
        pass

    def unsubscribe(self):
        pass


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello())
