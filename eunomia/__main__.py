import argparse
from eunomia import logger
from eunomia.tooling.dispatcher import Dispatcher


def main():
    parser = argparse.ArgumentParser(description='Installs configuration files for a given development tool')
    parser.add_argument('--config', type=str, help='Path to the eunomia configuration file', required=True)
    parser.add_argument('--destination', type=str, help='Path where to export the files', required=True)
    parser.add_argument('--level', default='DEBUG', type=str, help='Sets the level for the internal logs')
    args = parser.parse_args()
    logger.setLevel(level=args.level)
    Dispatcher.dispatch(config_path=args.config, destination=args.destination)
    return 0


if __name__ == "__main__":
    main()
