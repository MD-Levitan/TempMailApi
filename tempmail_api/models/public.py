import json

from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class Domains:
    domains: List[str]

    def __init__(self, data: list):
        self.domains = data


@dataclass
class Id:
    oid: str = None

    def __init__(self, data: dict):
        self.oid = data["$oid"]


@dataclass
class Date:
    numberLong: int = None

    def __init__(self, data: dict):
        self.numberLong = data["$numberLong"]


@dataclass
class CreatedAt:
    date: Date = None

    def __init__(self, data: dict):
        self.__dict__ = data
        self.date = None if data.get("$date", None) is None else Date(data["$date"])


@dataclass
class Message:
    _id: Id = None
    createdAt: CreatedAt = None
    mail_address_id: str = None
    mail_attachments_count: int = None
    mail_from: str = None
    mail_html: str = None
    mail_id: str = None
    mail_preview: str = None
    mail_subject: str = None
    #mail_text: NoneType = None
    mail_text_only: str = None
    mail_timestamp: float = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data
            self._id = None if data.get("_id", None) is None else Id(data["_id"])
            self.createdAt = None if data.get("createdAt", None) is None else CreatedAt(
                data["createdAt"])


@dataclass
class MessagesResponse:
    messages: List[Message] = None
    error: str = None

    def __init__(self, data):
        if isinstance(data, dict):
            self.__dict__ = data
        if isinstance(data, list):
            self.messages = list(map(lambda x: Message(x), data))