import os
from pybok.base import Base
from pybok.decorators import _constructor


class ConfigurationProperties(Base):
    def decorate(cls, arg):
        for field in cls.fields.keys():
            value = os.getenv(field.upper())
            if value is None and field in arg.__dict__:
                cls.fields[field] = arg.__dict__[field]
            elif field not in arg.__dict__ and value is None:
                raise ValueError(f"{field.upper()} is required.")
            else:
                cls.fields[field] = value

        _constructor(arg, default_fields=cls.fields)
