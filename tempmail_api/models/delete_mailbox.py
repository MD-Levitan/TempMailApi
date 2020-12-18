import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class DeleteEmail:
    sid: str = None
    email: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class DeleteEmailResponse:
    sid: str = None
    mailbox: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailboxDeleteRequest(JsonRpcRequest):
    method: str = "mailbox.delete"
    params: DeleteEmail = None

    def __init__(self, params: DeleteEmail):
        super().__init__(None)
        self.method = "mailbox.delete"
        self.params = params


@dataclass
class MailboxDeleteResponse(JsonRpcResponse):
    result: DeleteEmailResponse
     
    def __init__(self, params: dict):
        super().__init__(params)
        self.result = DeleteEmailResponse(self.result)