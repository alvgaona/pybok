from pybok.base import Base
from pybok.decorators import _no_init_fn


class UtilityClass(Base):
    def decorate(cls, arg):
        setattr(arg, '__init__', _no_init_fn())
