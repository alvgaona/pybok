from pybok.base import Base
from pybok.decorators import _setter_fn


class Setter(Base):
    def decorate(cls, arg):
        for field in cls.fields:
            setattr(arg, f'set_{field}', _setter_fn(field))
