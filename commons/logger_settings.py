import logging


def import_default_logger_settings():
    console_logger_settings()
    file_logger_settings()


def console_logger_settings():
    logFormatter = logging.Formatter('%(levelname)8s %(asctime)s [%(module)s] %(message)s')
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logFormatter)
    logger = logging.getLogger()
    logger.addHandler(consoleHandler)
    # root開到最大
    logger.setLevel(logging.NOTSET)


def file_logger_settings():
    logFormatter = logging.Formatter('%(levelname)8s %(asctime)s [%(module)s] %(message)s')
    fileHandler = logging.FileHandler('log.txt')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(logFormatter)
    logger = logging.getLogger()
    logger.addHandler(fileHandler)
    # root開到最大
    logger.setLevel(logging.NOTSET)
