from typing import Dict
from eunomia.model.language import Language
from eunomia.model.tool import ToolType
from eunomia.abstract.formatter import AbstractFormatter
from eunomia.abstract.factory import AbstractFactory
from eunomia.cpp.clang_format import ClangFormat


class FormatterFactory(AbstractFactory):

    __implementations: Dict[Language, AbstractFormatter] = {
        Language.Cpp: ClangFormat(),
        Language.Python: None,
    }

    def __init__(self) -> None:
        super().__init__(type=ToolType.Linter)

    def make(self, language: Language) -> AbstractFormatter:
        return self.__implementations[language]
