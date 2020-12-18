import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class DomainsResult:
    domains: List[str]

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class GetDomainsRequest(JsonRpcRequest):
    method: str = "getdomains"
    params: dict = None

    def __init__(self, params=None):
        super().__init__(None)
        self.method = "getdomains"
        self.params = dict()


@dataclass
class GetDomainsResponse(JsonRpcResponse):
    result: DomainsResult

    def __init__(self, params: dict):
        super().__init__(params)
        self.result = DomainsResult(self.result)
