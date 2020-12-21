import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class Listv2Params:
    sid: str = None
    onlyMailbox: bool = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class Listv2Result:
    sid: str = None
    mails: dict = None
    ordered_mails: List[str] = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailboxListRequest(JsonRpcRequest):
    method: str = "mailbox.listv2"
    params: Listv2Params = None

    def __init__(self, params: Listv2Params):
        super().__init__(None)
        self.method = "mailbox.listv2"
        self.params = params


@dataclass
class MailboxListResponse(JsonRpcResponse):
    result: Listv2Result
     
    def __init__(self, params: dict):
        super().__init__(params)
        self.result = Listv2Result(self.result)