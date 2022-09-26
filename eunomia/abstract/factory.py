from abc import ABC, abstractmethod
from eunomia.abstract.tool import AbstractTool
from eunomia.model.language import Language
from eunomia.model.tool import ToolType


class AbstractFactory(ABC):

    def __init__(self, type: ToolType) -> None:
        self._tyoe = type

    @property
    def type(self) -> ToolType:
        return self._type

    @abstractmethod
    def make(self, language: Language) -> AbstractTool:
        pass
