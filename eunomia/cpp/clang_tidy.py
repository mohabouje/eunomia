from typing import Any, Dict
from loguru import logger
from eunomia.abstract.linter import AbstractLinter
from eunomia.model.language import Language
from eunomia.resources import ToolResources, Resource, collect_resources


class ClangTidy(AbstractLinter):

    def __init__(self) -> None:
        super().__init__(Language.Cpp)

    def setup(self, configuration: Dict[str, Any], path: str) -> None:
        logger.info('Exporting a configuration for clang-tidy')
        resources: ToolResources = collect_resources(language=self.language,
                                                     type=self.type)
        for resource in resources:
            logger.debug(f'Exporting {resource.path} to {path}')
            result: str = resource.serialize(configuration=configuration)
            with open(f'{path}/.clang-tidy', 'w') as file:
                file.write(result)
