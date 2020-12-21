import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse

import json

from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class Mail:
    createdAt: str = None
    mail_address: str = None
    mail_address_id: str = None
    mail_from: str = None
    mail_html: str = None
    mail_id: str = None
    mail_preview: str = None
    mail_subject: str = None
    mail_source: str = None
    mail_text = None
    mail_text_only: str = None
    mail_timestamp: float = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class Messagesv2Params:
    sid: str = None
    email: str = None
    page: int = None
    limit: str = None
    password: str = None
    provider: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class Messagesv2Result:
    sid: str = None
    mailbox: str = None
    mails: List[Mail] = None
    page: int = None
    limit: int = None
    pages: int = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data
            self.mails = list(map(lambda x: Mail(x), data.get("mails", None)))


@dataclass
class MailboxMessagesRequest(JsonRpcRequest):
    method: str = "mailbox.messagesv2"
    params: Messagesv2Params = None

    def __init__(self, params: Messagesv2Params):
        super().__init__(None)
        self.method = "mailbox.messagesv2"
        self.params = params


@dataclass
class MailboxMessagesResponse(JsonRpcResponse):
    result: Messagesv2Result

    def __init__(self, params: dict):
        super().__init__(params)
        self.result = Messagesv2Result(self.result)