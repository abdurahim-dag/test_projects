from contextlib import asynccontextmanager

import aiohttp
import pytest

from . import models


@pytest.fixture(autouse=True)
def aiohttp_unix_connector(monkeypatch):
    def get_unix_connector(path: str):
        return models.UnixConnector(path=path)
    monkeypatch.setattr(aiohttp, "UnixConnector", get_unix_connector)


@pytest.fixture(autouse=True)
def aiohttp_client_session(monkeypatch):
    @asynccontextmanager
    async def get_client_session(connector: models.UnixConnector):
        yield models.ClientSession(connector=connector)
    monkeypatch.setattr(aiohttp, "ClientSession", get_client_session)
