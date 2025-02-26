import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def log(data, msg: str = None):
    logger.info('%s %s', data, msg)
