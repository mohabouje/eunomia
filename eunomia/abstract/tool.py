from abc import ABC, abstractmethod
from typing import Dict, Any
from eunomia.model.tool import ToolType
from eunomia.model.language import Language


class AbstractTool(ABC):

    def __init__(self, type: ToolType) -> None:
        self._type = type

    @property
    def type(self) -> ToolType:
        return self._type

    @abstractmethod
    def setup(self, configuration: Dict[str, Any], destination: str) -> None:
        pass


class AbstractToolForLanguage(AbstractTool):

    def __init__(self, type: ToolType, language: Language) -> None:
        super().__init__(type)
        self._language = language

    @property
    def language(self) -> Language:
        return self._language
