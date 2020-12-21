import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class ListCountParams:
    sid: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class ListCountResult:
    sid: str = None
    mails: dict = None  # Result {mail: count}
    ordered_mails: List[str] = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailboxListCountRequest(JsonRpcRequest):
    method: str = "mailbox.listv2.msg_count"
    params: ListCountParams = None

    def __init__(self, params: ListCountParams):
        super().__init__(None)
        self.method = "mailbox.listv2.msg_count"
        self.params = params


@dataclass
class MailboxListCountResponse(JsonRpcResponse):
    result: ListCountResult

    def __init__(self, params: dict):
        super().__init__(params)
        self.result = ListCountResult(self.result)