from dataclasses import dataclass


@dataclass
class PhotoSearchParams:
    count: str = "20"
    query: str = ""
    result_type: str = "recent"
    lang: str = "en"
    since_id: str = "0"
    max_id: str = "9999999999999999999"
    radius: str = "5mi"
    geocode: str = "43.161030,-77.610924,5mi"

    def __dict__(self):
        return {
            "count": self.count,
            "query": self.query,
            "result_type": self.result_type,
            "lang": self.lang,
            "since_id": self.since_id,
            "max_id": self.max_id,
            "radius": self.radius,
            "geocode": self.geocode,
        }


@dataclass
class PhotoSearch:
    headers: dict
    params: PhotoSearchParams
    api_url: str = "https://scraping.soax.com"
    endpoint_url: str = "v2/twitter/search/photos"

    def __init__(self, params: PhotoSearchParams):
        self.headers = {}
        self.params = params

    def __dict__(self):
        return {
            "api_url": self.api_url,
            "endpoint_url": self.endpoint_url,
            "headers": self.headers,
            "params": self.params,
        }
