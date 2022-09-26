import os
from typing import Any, Dict
from eunomia import logger
from eunomia.tooling.tool import AbstractTool
from eunomia.tooling.type import Type
from eunomia.resources.mustache import MustacheResource


class GitLint(AbstractTool):

    _default_path: str = os.path.join(os.path.dirname(__file__), 'template/gitlint.mustache')
    _default_filename: str = '.gitlint'
    _identifier: str = 'gitlint'

    def __init__(self) -> None:
        super().__init__(type=Type.Linter)

    def setup(self, configuration: Dict[str, Any], destination: str) -> None:
        file = os.path.join(destination, self._default_filename)
        logger.info(f'Exporting a configuration for gitlint in {file}')
        resource = MustacheResource(path=self._default_path)
        serialized: str = resource.serialize(configuration=configuration)
        with open(file, 'w') as file:
            file.write(serialized)
