import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse
from .messages_mailbox import Mail


@dataclass
class MailSourceParams:
    sid: str = None
    mail: str = None  # id of mail
    base64: bool = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailSourceResult:
    sid: str = None
    message: Mail = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailSourceRequest(JsonRpcRequest):
    method: str = "mail.source"
    params: MailSourceParams = None

    def __init__(self, params: MailSourceParams):
        super().__init__(None)
        self.method = "mail.source"
        self.params = params


@dataclass
class MailSourceResponse(JsonRpcResponse):
    result: MailSourceResult
     
    def __init__(self, params: dict):
        super().__init__(params)
        self.result = MailSourceResult(self.result)