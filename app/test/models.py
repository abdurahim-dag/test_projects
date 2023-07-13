import dataclasses
from contextlib import asynccontextmanager


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


@dataclasses.dataclass
class UnixConnector:
    path: str = '/var/run/docker.sock1'


@dataclasses.dataclass
class Response:
    content: AsyncIterator = AsyncIterator([b'test1', b'test2'])


@dataclasses.dataclass
class ClientSession:
    connector: UnixConnector | None = None

    @asynccontextmanager
    async def get(self, http_url: str):
        yield Response()
