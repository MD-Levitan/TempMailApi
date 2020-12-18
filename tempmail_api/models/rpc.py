import json

from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class JsonRpcMessage:
    jsonrpc: str = "2.0"  # jsonrpc ptocol vereiosn
    id: str = "jsonrpc"

    def __init__(self, data: dict):
        if data is not None:
            self.jsonrpc = data.get("jsonrpc", "2.0")
            self.id = data.get("id", "jsonrpc")
        else:
            self.jsonrpc = "2.0"
            self.id = "jsonrpc"

    def json(self) -> dict:
        return {"jsonrpc": self.jsonrpc, "id": self.id}


@dataclass
class JsonRpcRequest(JsonRpcMessage):
    method: str = None  # protocol method
    params: dict = None  # dict with params for method

    def __init__(self, data: dict):
        super().__init__(data)
        if data is not None:
            self.method = data.get("method", None)
            self.params = data.get("params", None)

    def json(self) -> dict:
        result = super().json()
        result.update(self.__dict__)
        if self.params is None:
            result.update({"params": dict()})
        return json.dumps(result)


@dataclass
class Error:
    code: int = None
    subCode = None
    message: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class JsonRpcResponse(JsonRpcMessage):
    result: dict = None  # dict with result
    error: dict = None

    def __init__(self, data: dict):
        super().__init__(data)
        if data is not None:
            self.result = data.get("result", None)
            self.error = Error(data.get("error", None))
