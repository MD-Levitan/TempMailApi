import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class EmailParams:
    domain: str = None
    email: str = None
    sid: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


# @dataclass
# class EmailParamsResponse:
#     # domain: str = None
#     email: str = None
#     sid: str = None

#     def __init__(self, data: dict):
#         if data is not None:
#             self.__dict__ = data


@dataclass
class NewMailboxRequest(JsonRpcRequest):
    method: str = "mailbox.new"
    params: EmailParams = None

    def __init__(self, params: EmailParams):
        super().__init__(None)
        self.method = "mailbox.new"
        self.params = params


@dataclass
class NewMailboxResponse(JsonRpcResponse):
    result: EmailParams #EmailParamsResponse

    def __init__(self, params: dict):
        super().__init__(params)
        self.result = EmailParams(self.result)
