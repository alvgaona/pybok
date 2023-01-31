from abc import ABC, abstractmethod


class Base(ABC):
    fields = {}
    kwargs = None
    args = None

    def _init_fields(cls):
        fields = {}

        for field in cls.__annotations__.keys():

            if field in cls.__dict__:
                fields[field] = cls.__dict__[field]
            else:
                fields[field] = None

        return fields

    def __new__(cls, arg=None, *args, **kwargs):
        """
        HACK: I really don't know how this is working but it works
        to support decorators with args.

        All I know that for each decorator, its __new__ method is called
        twice when it receives arguments. For some reason, this makes it
        possible that the decorator method gets the decorated class, and
        the decorator arguments.
        """
        if arg is not None:
            cls.fields = cls._init_fields(arg)
            cls.decorate(cls, arg)
            return arg
        else:
            cls.args = args
            cls.kwargs = kwargs
            return cls

    @abstractmethod
    def decorate(cls, arg, **kwargs):
        pass
