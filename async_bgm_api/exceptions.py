import aiohttp


class ServerConnectionError(Exception):
    def __init__(
        self,
        request: aiohttp.RequestInfo = None,
        response: aiohttp.ClientResponse = None,
        raw_exception: Exception = None,
    ):
        self.request = request
        self.response = response
        self.raw = raw_exception


class RecordNotFound(Exception):
    def __init__(
        self,
        request: aiohttp.RequestInfo = None,
        response: aiohttp.ClientResponse = None,
        raw_exception: Exception = None,
    ):
        self.request = request
        self.response = response
        self.raw = raw_exception
