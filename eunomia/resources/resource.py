from typing import Dict, Any
from abc import ABC, abstractmethod


class Resource(ABC):

    def __init__(self, path: str) -> None:
        self.path_ = path

    @property
    def path(self) -> str:
        return self.path_

    @abstractmethod
    def serialize(self, configuration: Dict[str, Any]) -> str:
        pass
