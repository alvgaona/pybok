from pybok.base import Base
from pybok.decorators import _eq_fn, _hash_fn


class EqualsAndHashCode(Base):
    def decorate(cls, arg):
        setattr(arg, '__eq__', _eq_fn())
        setattr(arg, '__hash__', _hash_fn(cls.fields))
