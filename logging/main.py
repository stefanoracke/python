import logging
import logging.config
import traceback

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')

logger.debug('This is a debug Message')

