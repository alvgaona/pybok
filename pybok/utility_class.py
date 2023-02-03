from pybok.base import Base
from pybok.decorators import _no_init_fn


class UtilityClass(Base):
    def __new__(cls, arg=None, *args, **kwargs):
        """
        NOTE: redifined from parent class.
        """
        if arg is not None:
            cls.decorate(cls, arg)
            return arg
        else:
            cls.args = args
            cls.kwargs = kwargs
            return cls

    def decorate(cls, arg):
        setattr(arg, '__init__', _no_init_fn())
