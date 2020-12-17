import requests
import json

from dataclasses import dataclass
from typing import List, Optional, Any
from .utils import encrypt


def create_seesion(proxy: dict = None, verify: bool = True):
    session = requests.Session()

    if proxy is not None:
        session.proxies.update(proxy)
        session.verify = verify

    session.headers.update({"Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/3.14.7"})
    return session


class API:
    URL = "https://mob1.temp-mail.org"
    SESSION = create_seesion()

    @staticmethod
    def get_domains():
        """! Get all valide domains.
        

        GET /request/domains/format/json HTTP/1.1
        Accept: application/json
        Host: mob1.temp-mail.org
        Connection: close
        Accept-Encoding: gzip, deflate
        User-Agent: okhttp/3.14.7
        """
        url = API.URL + "/request/domains/format/json"
        r = API.SESSION.get(url)

        if r.status_code == 404:
            raise Exception("response status: 404")

        return Domains(json.loads(r.text))

    @staticmethod
    def get_messages(email: str):
        """! Get messages by email.
        

        GET /request/mail/id/x6LGscemxr3Hp8emxrzGs8emxr3Gt8egx6LGtca3xrXGsMelx6LGsMa8xrbGtseixrzGsMenxrPGsMayx6bHpQ==/format/json HTTP/1.1
        Host: mob1.temp-mail.org
        User-Agent: okhttp/3.14.7
        Accept-Encoding: gzip, deflate
        Accept: application/json
        Connection: close
        """
        url = API.URL + "/request/mail/id/{}/format/json".format(encrypt(email))
        r = API.SESSION.get(url)

        if r.status_code == 404:
            raise Exception("response status: 404")

        return MessagesResponse(json.loads(r.text))

    # "/request/validate_domain/{base64_enc_domain}/format/json"
    # "/rpc/"
    # "/request/mail/id/{email}/format/json"
    # "/request/source/id/{emailId}/format/json"
    # "/request/one_attachment/id/{mail_id}/{attachment_number}/format/json"

    #         arrayList.add("/request/domains/");
    #     arrayList.add("/request/mail/id/");
    #     arrayList.add("/request/source/id/");
    #     arrayList.add("/request/one_attachment/id/");
    #     arrayList.add("/request/validate_domain/");"


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