from pybok.base import Base
from pybok.decorators import _getter_fn

class Getter(Base):
    def decorate(cls, arg):
        for field in cls.fields:
            setattr(arg, f'get_{field}', _getter_fn(field))
