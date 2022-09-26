import os
from typing import Any, Dict
from eunomia import logger
from eunomia.tooling.tool import AbstractTool
from eunomia.tooling.type import Type
from eunomia.resources.mustache import MustacheResource


class GitIgnore(AbstractTool):

    _default_path: str = os.path.join(os.path.dirname(__file__), 'template/gitignore.mustache')
    _default_filename: str = '.gitignore'
    _identifier: str = 'gitignore'

    def __init__(self) -> None:
        super().__init__(type=Type.Linter)

    def setup(self, configuration: Dict[str, Any], destination: str) -> None:
        logger.info('Exporting a configuration for gitlint in {file}')
