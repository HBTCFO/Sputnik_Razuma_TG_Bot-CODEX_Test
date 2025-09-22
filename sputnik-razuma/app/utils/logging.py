import logging
import os
from loguru import logger

def setup_logging():
    # Перенаправляем стандартный logging в loguru
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            try:
                level = logger.level(record.levelname).name
            except Exception:
                level = record.levelno
            logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())

    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO, force=True)
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level="INFO", serialize=False)

setup_logging()
