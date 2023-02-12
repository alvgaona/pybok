import re
from json import dumps

from pybok.base import Base


def remove_prefix(attributes):
    new_dict = {}

    for k, v in attributes.items():
        new_dict[re.sub('^_', '', k)] = v

    return new_dict


class ToJSON(Base):
    def json(self):
        return dumps(remove_prefix(self.__dict__), default=lambda o: remove_prefix(o.__dict__), indent=4)

    def decorate(cls, arg):
        setattr(arg, 'json', cls.json)
