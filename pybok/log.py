import logging
import logging.config
import json
from pybok.base import Base


class Config:
    _CONFIG_FILE = 'logger.json'

    config = None

    def __init__(self) -> None:
        if self.config is None:
            with open(self._CONFIG_FILE, 'r') as f:
                config = json.load(f)

            logging.config.dictConfig(config)


class Log(Base):
    def decorate(cls, arg):
        setattr(arg, 'logger', logging.getLogger())


config = Config()
