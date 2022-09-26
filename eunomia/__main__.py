import argparse
import yaml
from loguru import logger

from eunomia.model.language import Language
from eunomia.model.tool import ToolType

from eunomia.factory.dispatcher import Dispatcher
from eunomia.abstract.factory import AbstractFactory
from eunomia.abstract.tool import AbstractTool


def main():
    parser = argparse.ArgumentParser(description='Installs configuration files for a given development tool')
    parser.add_argument('--language', type=Language.argparse, choices=list(Language), required=True)
    parser.add_argument('--type', type=ToolType.argparse, choices=list(ToolType), required=True)
    parser.add_argument('--path', type=str, help='Path to the project', required=True)
    parser.add_argument('--config', type=str, help='Path to the configuration file', required=True)

    args = parser.parse_args()

    try:
        with open(args.config, "r") as config:
            configuration = yaml.safe_load(config)
    except yaml.YAMLError as exc:
        logger.error(f'Configuration file {args.config} could not be parsed.')
        logger.error(exc)
        return

    logger.debug(f'Generating {args.type} configuration file for {args.language} in {args.path}')
    factory: AbstractFactory = Dispatcher().make(args.type)
    tooling: AbstractTool = factory.make(args.language)
    tooling.setup(configuration=configuration, path=args.path)
    return 0


if __name__ == "__main__":
    main()
