
import logging


def __setup_logger():
    logger = logging.getLogger('eunomia')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = __setup_logger()
