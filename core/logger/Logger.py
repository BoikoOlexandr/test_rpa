import logging

from core.logger.loggerFormat import LoggerFormat


def set_file_log():
    log_handler = logging.FileHandler("output/RPA.log")
    log_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s-%(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
    )
    log.addHandler(log_handler)


def set_stream_log():
    log_window_handler = logging.StreamHandler()
    log_window_handler.setFormatter(
        LoggerFormat('%(asctime)s - %(name)s-%(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
    )
    log.addHandler(log_window_handler)


log = logging.getLogger("RPA")
set_stream_log()
set_file_log()
log.setLevel(logging.INFO)
