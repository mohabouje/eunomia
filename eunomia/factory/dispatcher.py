from typing import Dict
from eunomia.abstract.factory import AbstractFactory
from eunomia.factory.linter import LinterFactory
from eunomia.factory.formatter import FormatterFactory
from eunomia.model.tool import ToolType


class Dispatcher:

    __implementations__: Dict[ToolType, AbstractFactory] = {
        ToolType.Linter: LinterFactory(),
        ToolType.Formatter: FormatterFactory(),
    }

    def make(self, type: ToolType) -> AbstractFactory:
        return self.__implementations__[type]
