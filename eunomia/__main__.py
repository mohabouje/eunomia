import argparse
import yaml
import os

from loguru import logger
from typing import Any, Dict
from eunomia.model.language import Language
from eunomia.model.tool import ToolType
from eunomia.factory.dispatcher import Dispatcher
from eunomia.abstract.factory import AbstractFactory
from eunomia.abstract.tool import AbstractTool


def read_configuration(path: str) -> Dict[str, Any]:
    logger.info(f'Reading eunomia configuration from {path}')
    try:
        with open(path, "r") as config:
            configuration = yaml.safe_load(config)
    except yaml.YAMLError as exc:
        logger.error(f'Configuration file {path} could not be parsed.')
        logger.error(exc)
        return
    return configuration


def main():
    default_config = os.path.join(os.getcwd(), '.eunomiarc')
    parser = argparse.ArgumentParser(description='Installs configuration files for a given development tool')
    parser.add_argument('--language', type=Language.argparse, choices=list(Language), required=True)
    parser.add_argument('--type', type=ToolType.argparse, choices=list(ToolType), required=True)
    parser.add_argument('--destination', type=str, help='Path where to export the files', required=True)
    parser.add_argument('--config', default=default_config, type=str,
                        help='Path to the eunomia configuration file', required=True)

    args = parser.parse_args()

    configuration = read_configuration(path=args.config)
    logger.info(f'Generating {args.type} configuration file for {args.language} in {args.destination}')
    factory: AbstractFactory = Dispatcher().make(args.type)
    tooling: AbstractTool = factory.make(args.language)
    tooling.setup(configuration=configuration, destination=args.destination)
    return 0


if __name__ == "__main__":
    main()
