from abc import ABC, abstractmethod
from typing import List


class Scraper(ABC):
    @abstractmethod
    def manualLimitOverride(self, limit: int) -> None:
        pass

    @property
    @abstractmethod
    def limit(self):
        pass
