import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class UserLoginParams:
    username: str = None
    password: str = None
    provider: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class UserLoginResult:
    sid: str = None
    cancel_url: str = None
    update_url: str = None
    username: str = None
    subscriptionEndDate: int = None
    paddle_status: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class UserLoginRequest(JsonRpcRequest):
    method: str = "user.login"
    params: UserLoginParams = None

    def __init__(self, params: UserLoginParams):
        super().__init__(None)
        self.method = "user.login"
        self.params = params


@dataclass
class UserLoginResponse(JsonRpcResponse):
    result: UserLoginResult

    def __init__(self, params: dict):
        super().__init__(params)
        self.result = UserLoginResult(self.result)
