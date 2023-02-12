import json
import logging
import logging.config
import os

from pybok.base import Base


class Config:
    _CONFIG_FILE = 'logger.json'

    config = None

    def __init__(self) -> None:
        if self.config is None:
            base_path = os.path.abspath(os.getcwd())

            with open(os.path.join(base_path, self._CONFIG_FILE), 'r') as f:
                config = json.load(f)

            logging.config.dictConfig(config)


class Log(Base):
    def decorate(cls, arg):
        setattr(arg, 'logger', logging.getLogger())


# config = Config()
