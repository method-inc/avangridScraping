from dataclasses import dataclass
from abc import ABC
from os import path, environ


@dataclass(order=True)
class SoaxRequest(ABC):
    base_url: str
    endpoint_url: str
    headers: dict
    params: dict

    def __init__(self, base_url: str, endpoint_url: str, params: dict):
        self.base_url = base_url
        self.endpoint_url = endpoint_url
        self.headers = {}
        self.params = params
        self.headers["X-SOAX-API-Secret"] = environ.get("X-SOAX-API-KEY")

    def __repr__(self):
        return (
            path.join(self.base_url, self.endpoint_url)
            + f"\nheaders: {self.headers}, params: {self.params}"
        )
