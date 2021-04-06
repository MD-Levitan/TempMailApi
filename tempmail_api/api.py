import requests
import json

from functools import wraps
from dataclasses import dataclass
from typing import List, Optional, Any
from .utils import encrypt

from .models.public import *
from .models.rpc import *
from .models.new_mailbox import *
from .models.user_login import *
from .models.messages_mailbox import *
from .models.delete_mailbox import *
from .models.domains import *
from .models.list_mailbox import *
from .models.listcount_mailbox import *
from .models.mail_source import *


def create_session(proxy: dict = None, verify: bool = True) -> requests.Session:
    session = requests.Session()

    if proxy is not None:
        session.proxies.update(proxy)
        session.verify = verify

    session.headers.update({"Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/3.14.7"})
    return session


class API:
    URL = "https://mob1.temp-mail.org"
    SESSION = create_session()

    @staticmethod
    def get_domains(session: requests.Session=None):
        """! Get all valide domains.
        

        GET /request/domains/format/json HTTP/1.1
        Accept: application/json
        Host: mob1.temp-mail.org
        Connection: close
        Accept-Encoding: gzip, deflate
        User-Agent: okhttp/3.14.7
        """
        session_ = session if session is not None else API.SESSION

        url = API.URL + "/request/domains/format/json"
        r = session_.get(url)

        if r.status_code == 404:
            raise Exception("response status: 404")

        return Domains(json.loads(r.text))

    @staticmethod
    def get_messages(email: str, session: requests.Session=None):
        """! Get messages by email.
        

        GET /request/mail/id/x6LGscemxr3Hp8emxrzGs8emxr3Gt8egx6LGtca3xrXGsMelx6LGsMa8xrbGtseixrzGsMenxrPGsMayx6bHpQ==/format/json HTTP/1.1
        Host: mob1.temp-mail.org
        User-Agent: okhttp/3.14.7
        Accept-Encoding: gzip, deflate
        Accept: application/json
        Connection: close
        """
        session_ = session if session is not None else API.SESSION

        url = API.URL + "/request/mail/id/{}/format/json".format(encrypt(email))
        r = session_.get(url)

        if r.status_code == 404:
            raise Exception("response status: 404")

        return MessagesResponse(json.loads(r.text))


def rpc(request_class, response_class):
    def rpc_decorator(func):
        @wraps(func)
        def rpc_wrapper(**kwargs):
            if "session" in kwargs:
                session = kwargs.pop("session")
            else:
                session = PremiumAPI.SESSION

            url = PremiumAPI.URL + "/rpc/"

            r = session.post(url, data=request_class(kwargs).json())

            if r.status_code == 404:
                raise Exception("response status: 404")

            return response_class(json.loads(r.text))

        return rpc_wrapper

    return rpc_decorator


class PremiumAPI:
    URL = "https://papi2.temp-mail.org"
    SESSION = create_session()

    @staticmethod
    def send_rpc(request: JsonRpcRequest, session: requests.Session=None):
        """! Send rpc request. """
        url = PremiumAPI.URL + "/rpc/"
        r = PremiumAPI.SESSION.post(url, data=json.dumps(request.json()))

        if r.status_code == 404:
            raise Exception("response status: 404")

        return JsonRpcResponse(json.loads(r.text))

    @rpc(NewMailboxRequest, NewMailboxResponse)
    @staticmethod
    def new_mailbox(sid: str, email: str, domain: str):
        pass

    @rpc(UserLoginRequest, UserLoginResponse)
    @staticmethod
    def user_login(username: str, password: str, provider: str = "paddle"):
        pass

    @rpc(MailboxMessagesRequest, MailboxMessagesResponse)
    @staticmethod
    def mailbox_messages(sid: str, email: str, page: int = 1, limit: str = "10"):
        pass

    @rpc(MailboxDeleteRequest, MailboxDeleteResponse)
    @staticmethod
    def mailbox_delete(sid: str, email: str):
        pass

    @rpc(GetDomainsRequest, GetDomainsResponse)
    @staticmethod
    def get_domains():
        pass

    @rpc(MailboxListRequest, MailboxListResponse)
    @staticmethod
    def mailbox_list(sid: str):
        pass
    
    @rpc(MailboxListCountRequest, MailboxListCountResponse)
    @staticmethod
    def mailbox_list_count(sid: str):
        pass

    @rpc(MailSourceRequest, MailSourceResponse)
    @staticmethod
    def mail_source(sid: str, mail:str, base64: bool):
        pass