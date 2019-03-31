日志的级别：

从左至右级别越来越高

`DEBUG、INFO、WARNING、ERROR、CRITICAL`





`logger`日志收集器，在源码中默认指定了收集器的名称为`root，info、error、warning`等

`handler`日志输出渠道



```python
import logging

# 如果没有设置日志级别，那么logging默认级别是warning
logging.basicConfig(filename='log.log',level=logging.DEBUG)

logging.debug('hello debug')
logging.info('hello info')
logging.warning('hello warning')
logging.error('hello error')
logging.critical('hello critical')
```



#### 封装`logging`类

```python
import logging

class LogRecorder:

    def get_logger(self,msg,level):
        logger = logging.getLogger('my_logger')
        logger.setLevel('DEBUG')

        format = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setLevel('DEBUG')
        console_handler.setFormatter(format)

        file_handler = logging.FileHandler('my_logger.log',encoding='utf-8')
        file_handler.setLevel('DEBUG')
        file_handler.setFormatter(format)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        if level=='DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)

        # 如果日志出现重复，那么需要removehandler
        logger.removeHandler(console_handler)
        logger.removeHandler(file_handler)

    def debug(self,msg):
        self.get_logger(msg,'DEBUG')

    def info(self,msg):
        self.get_logger(msg,'INFO')

    def warning(self,msg):
        self.get_logger(msg,'WARNING')

    def error(self,msg):
        self.get_logger(msg,'ERROR')

    def critical(self,msg):
        self.get_logger(msg,'CRITICAL')


if __name__ == '__main__':
    logger = LogRecorder()
    logger.error('这是谁的')
```