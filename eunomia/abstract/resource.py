from typing import NewType, Dict, Any
from abc import ABC, abstractmethod
from eunomia.model.language import Language
from eunomia.model.tool import ToolType


class Resource(ABC):

    def __init__(self, type: ToolType, language: Language, path: str) -> None:
        self.type_ = type
        self.language_ = language
        self.path_ = path

    @property
    def type(self) -> ToolType:
        return self.type_

    @property
    def language(self) -> Language:
        return self.language_

    @property
    def path(self) -> str:
        return self.path_

    @abstractmethod
    def serialize(self, configuration: Dict[str, Any]) -> str:
        pass
