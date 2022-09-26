from typing import Dict, Any
from eunomia.resources.resource import Resource
from chevron import render


class MustacheResource(Resource):

    def __init__(self, path: str) -> None:
        super().__init__(path=path)

    def serialize(self, configuration: Dict[str, Any]) -> str:
        with open(self.path, 'r') as file:
            return render(file, configuration)
