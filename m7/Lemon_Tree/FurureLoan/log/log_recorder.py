import logging
from settings import LOG_FILE

class LogRecorder:

    def get_logger(self,msg,level):
        logger = logging.getLogger('web')
        logger.setLevel('DEBUG')

        format = logging.Formatter('%(levelname)s :%(asctime)s %(filename)s %(lineno)s %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setLevel('DEBUG')
        console_handler.setFormatter(format)

        file_handler = logging.FileHandler(filename=LOG_FILE,encoding='utf-8')
        file_handler.setLevel('DEBUG')
        file_handler.setFormatter(format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        elif level == 'critical':
            logger.critical(msg)

        logger.removeHandler(console_handler)
        logger.removeHandler(file_handler)

    def debug(self,msg):
        self.get_logger(msg,'debug')

    def info(self,msg):
        self.get_logger(msg,'info')

    def warning(self,msg):
        self.get_logger(msg,'warning')

    def error(self,msg):
        self.get_logger(msg,'info')

    def critical(self,msg):
        self.get_logger(msg,'critical')


