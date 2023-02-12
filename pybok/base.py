from abc import ABC, abstractmethod

from pybok.property import Property


class Field:
    def __init__(self, name, value, type) -> None:
        self._name,
        self._value,
        self._type

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type


class Base(ABC):
    fields = {}
    super_fields = {}
    kwargs = None
    args = None

    def _init_fields(cls):
        fields = {}
        super_fields = {}

        annotations = cls.__annotations__ if len(cls.__mro__) <= 2 else { k: v for k, v in cls.__annotations__.items() }

        for c in cls.__mro__[1:]:
            if '__annotations__' in c.__dict__:
                for field in c.__annotations__.keys():
                    if field in c.__dict__ and not isinstance(c.__dict__[field], Property):
                        super_fields[field] = c.__dict__[field]
                    else:
                        super_fields[field] = None

        for field in annotations.keys():
            if field in cls.__dict__ and not isinstance(cls.__dict__[field], Property):
                fields[field] = cls.__dict__[field]
            else:
                fields[field] = None

        return fields, super_fields

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
            cls.fields, cls.super_fields = cls._init_fields(arg)
            cls.decorate(cls, arg)
            return arg
        else:
            cls.args = args
            cls.kwargs = kwargs
            return cls

    @abstractmethod
    def decorate(cls, arg, **kwargs):
        pass
