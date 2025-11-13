import logging
import os
import sys
from logging import Logger

from MCModUpdater.src.cli.utills.screen import get_app_version
from MCModUpdater.src.core.constants import APP_NAME, CONFIG_DIR_PATH, LOG_FILE_PATH


_logger: Logger = logging.getLogger(APP_NAME)
_already_logged_info: bool = False

if not os.path.exists(CONFIG_DIR_PATH):
    os.makedirs(CONFIG_DIR_PATH, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    style="{",
    datefmt="%H:%M:%S",
    format="[{asctime:s}.{msecs:0>3.0f} - {levelname: >8s}]: {message:s}",
    handlers=[
        logging.FileHandler(filename=LOG_FILE_PATH, mode="w"),
        logging.StreamHandler(sys.stdout),
    ],
)


def get_logger() -> Logger:
    global _already_logged_info

    if not _already_logged_info:
        _logger.info(get_app_version())
        _already_logged_info = True
    return _logger
