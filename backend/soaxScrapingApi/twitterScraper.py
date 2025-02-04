import requests
import json

from urllib.parse import urljoin

from backend.Scraper import Scraper
from backend.soaxScrapingApi.twitterRequests.photoSearch import (
    PhotoSearch,
    PhotoSearchParams,
)
from backend.soaxScrapingApi.SoaxRequest import SoaxRequest


class SoaxTwitterPhotos(SoaxRequest, Scraper):
    _req = None
    req_limit = 1

    def __init__(self, obj: PhotoSearch):
        super().__init__(
            base_url=PhotoSearch.api_url,
            endpoint_url=PhotoSearch.endpoint_url,
            params=obj.params.__dict__(),
        )

    def _init_request(self):
        full_url = urljoin(self.base_url, self.endpoint_url)
        self._req = requests.Request(
            method="GET", url=full_url, params=self.params, headers=self.headers
        )

    def replaceParams(self, params: PhotoSearchParams):
        self.params = params.__dict__()

    def twitterHashtagSearchRequest(self):
        if not self._req:
            self._init_request()

        # check that required parameters are present
        if "query" not in self.params:
            raise ValueError("query parameter is required")
        if "since_id" not in self.params:
            raise ValueError("since_id parameter is required")
        if "max_id" not in self.params:
            raise ValueError("max_id parameter is required")
        if "result_type" not in self.params:
            raise ValueError("result_type parameter is required")
        if "count" not in self.params:
            raise ValueError("count parameter is required")
        if "radius" not in self.params:
            raise ValueError("radius parameter is required")
        if "geocode" not in self.params:
            raise ValueError("geocode parameter is required")

        return self._req

    def run(self, func):
        if self.limit() <= 0:
            self.manualLimitOverride(1)
        req = func().prepare()
        assert isinstance(req, requests.PreparedRequest), "Invalid request object"
        with requests.Session() as session:
            response = session.send(req)
        with open("cache/cahce.txt", "a") as file:
            file.write(json.dumps(response.json()))
        self.req_limit -= 1
        return response.json()

    def limit(self):
        return self.req_limit

    def manualLimitOverride(self, limit: int):
        i = input("Intended limit reached, manually override to continue? [y/n]")
        if i.lower() == "y":
            self.req_limit = limit
