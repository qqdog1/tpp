from logging.config import fileConfig


def set_logger_by_config():
    fileConfig('../logging_config.txt')