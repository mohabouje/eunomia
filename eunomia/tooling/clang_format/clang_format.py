import os
from typing import Any, Dict
from eunomia import logger
from eunomia.tooling.tool import AbstractTool
from eunomia.tooling.type import Type
from eunomia.resources.mustache import MustacheResource


class ClangFormat(AbstractTool):

    _default_path: str = os.path.join(os.path.dirname(__file__), 'template/clang-format.mustache')
    _default_filename: str = '.clang-format'
    _identifier: str = 'clang-format'

    def __init__(self) -> None:
        super().__init__(type=Type.Formatter)

    def setup(self, configuration: Dict[str, Any], destination: str) -> None:
        file = os.path.join(destination, self._default_filename)
        logger.info(f'Exporting a configuration for clang-format in {file}')
        resource = MustacheResource(path=self._default_path)
        serialized: str = resource.serialize(configuration=configuration)
        with open(file, 'w') as file:
            file.write(serialized)
