from typing import Dict, Any
from eunomia.abstract.resource import Resource
from eunomia.model.language import Language
from eunomia.model.tool import ToolType
from chevron import render


class MustacheResource(Resource):

    def __init__(self, type: ToolType, language: Language, path: str) -> None:
        super().__init__(type, language, path=path)

    def serialize(self, configuration: Dict[str, Any]) -> str:
        with open(self.path, 'r') as file:
            return render(file, configuration)
