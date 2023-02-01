from pybok.base import Base
from pybok.decorators import _to_string_fn


class ToString(Base):
    def decorate(cls, arg):
        setattr(arg, '__repr__', _to_string_fn(cls.fields))
