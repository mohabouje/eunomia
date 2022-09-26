import os
from typing import NewType, Dict, List
from eunomia.abstract.resource import Resource
from eunomia.resources.mustache import MustacheResource
from eunomia.model.language import Language
from eunomia.model.tool import ToolType

ToolResources = NewType('ToolResources', List[Resource])
LanguageResources = NewType('LanguageResources', Dict[Language, Dict[ToolType, Resource]])

__root = os.path.dirname(os.path.abspath(__file__))
def __path(x): return os.path.join(__root, x)


__resources: LanguageResources = {
    Language.Cpp: {
        ToolType.Formatter: [MustacheResource(type=ToolType.Formatter, language=Language.Cpp, path=__path('cpp/clang-format.mustache'))],
        ToolType.Linter: [MustacheResource(type=ToolType.Linter, language=Language.Cpp, path=__path('cpp/clang-tidy.mustache'))],
    },
    Language.Python: {
        ToolType.Formatter: None,
        ToolType.Linter: None,
    },
}


def collect_resources(language: Language, type: ToolType) -> ToolResources:
    return __resources[language][type]
