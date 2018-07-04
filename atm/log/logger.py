import logging
from logging import handlers

logger = logging.getLogger('ATM')
logger.setLevel(logging.INFO)

file_handler = handlers.RotatingFileHandler(
    filename = '../log/logger.log',maxBytes = 1000,backupCount = 3,encoding = 'utf-8')

logger.addHandler(file_handler)

file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

file_handler.setFormatter(file_formatter)