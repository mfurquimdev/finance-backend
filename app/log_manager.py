import logging
import sys
import app.parameter as parameter

logging_level = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


class Logging():

    def __init__(self):
        self.root = logging.getLogger()
        self.root.setLevel(logging_level.get(parameter.get_env('LOG_LEVEL')))

        self.ch = logging.StreamHandler(sys.stdout)
        self.ch.setLevel(logging_level.get(parameter.get_env('LOG_LEVEL')))
        self.formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s [%(process)d]: %(message)s')
        self.ch.setFormatter(self.formatter)
        self.root.addHandler(self.ch)

    def debug(self, text):
        self.root.debug(str(text).replace('\n', ' | '))

    def info(self, text):
        self.root.info(str(text).replace('\n', ' | '))

    def warning(self, text):
        self.root.warning(str(text).replace('\n', ' | '))

    def error(self, text):
        self.root.error(str(text).replace('\n', ' | '))

    def critical(self, text):
        self.root.critical(str(text).replace('\n', ' | '))

    def exception(self, text):
        self.root.exception(str(text).replace('\n', ' | '))


log = Logging()
