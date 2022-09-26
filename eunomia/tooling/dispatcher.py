import yaml
from typing import Dict, List, Any
from eunomia import logger
from eunomia.tooling.clang_format.clang_format import ClangFormat
from eunomia.tooling.clang_tidy.clang_tidy import ClangTidy
from eunomia.tooling.gitlint.gitlint import GitLint
from eunomia.tooling.gitignore.gitignore import GitIgnore
from eunomia.tooling.tool import AbstractTool


class Dispatcher(object):
    __tools: List[AbstractTool] = [ClangFormat(), ClangTidy(), GitLint(), GitIgnore()]
    __hashing: Dict[str, AbstractTool] = dict([(tool._identifier, tool) for tool in __tools])

    @staticmethod
    def parse_configuration(config_path: str) -> Dict[str, Any]:
        logger.info(f'Reading eunomia configuration from {config_path}')
        try:
            with open(config_path, "r") as config:
                configuration = yaml.safe_load(config)
        except yaml.YAMLError as exc:
            logger.error(f'Configuration file {config_path} could not be parsed.')
            logger.error(exc)
            return
        return configuration

    @staticmethod
    def dispatch(config_path: str, destination: str) -> None:
        configuration = Dispatcher.parse_configuration(config_path=config_path)
        for identifier in configuration.keys():
            if identifier not in Dispatcher.__hashing:
                logger.warn(f'Found an unrecognized idenfier ({identifier}) in {config_path}')
                continue

            tool = Dispatcher.__hashing[identifier]
            tool.setup(configuration=configuration[identifier], destination=destination)
