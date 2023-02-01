import logging

from core.logger.loggerFormat import LoggerFormat


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        log = logging.getLogger("RPA")
        log.setLevel(logging.INFO)
        self.set_stream_log(log)
        self.set_file_log(log)
        self.log = log

    def get_logger(self):
        return self.log

    def set_log_format(self):
        return logging.Formatter('%(asctime)s - %(name)s-%(levelname)s - %(message)s (%(filename)s:%(lineno)d)')

    def set_file_log(self, log):
        log_handler = logging.FileHandler("output/RPA.log")
        log_handler.setFormatter(self.set_log_format())
        log.addHandler(log_handler)

    def set_stream_log(self, log):
        log_window_handler = logging.StreamHandler()
        log_window_handler.setFormatter(
            LoggerFormat('%(asctime)s - %(name)s-%(levelname)s - %(message)s (%(filename)s:%(lineno)d)'))
        log.addHandler(log_window_handler)

