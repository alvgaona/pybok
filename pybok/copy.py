from copy import copy, deepcopy

from pybok.base import Base


class Copy(Base):
    def copy(self):
        return copy(self)

    def deepcopy(self):
        return deepcopy(self)

    def decorate(cls, arg):
        setattr(arg, 'copy', cls.copy)
        setattr(arg, 'deepcopy', cls.deepcopy)
