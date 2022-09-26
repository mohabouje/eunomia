from typing import Dict
from eunomia.model.language import Language
from eunomia.model.tool import ToolType
from eunomia.abstract.linter import AbstractLinter
from eunomia.abstract.factory import AbstractFactory
from eunomia.cpp.clang_tidy import ClangTidy


class LinterFactory(AbstractFactory):

    __implementations: Dict[Language, AbstractLinter] = {
        Language.Cpp: ClangTidy(),
        Language.Python: None,
    }

    def __init__(self) -> None:
        super().__init__(type=ToolType.Linter)

    def make(self, language: Language) -> AbstractLinter:
        return self.__implementations[language]
