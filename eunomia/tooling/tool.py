from abc import ABC, abstractmethod
from typing import Dict, Any
from eunomia.tooling.type import Type


class AbstractTool(ABC):

    _default_path: str = None
    _default_filename: str = None
    _identifier: str = None

    def __init__(self, type: Type) -> None:
        self._type = type

    @property
    def type(self) -> Type:
        return self._type

    @abstractmethod
    def setup(self, configuration: Dict[str, Any], destination: str) -> None:
        pass
