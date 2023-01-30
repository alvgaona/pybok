from abc import ABC, abstractmethod

class Base(ABC):
    fields = {}

    def _init_fields(cls):
        fields = {}

        for field in cls.__annotations__.keys():
            if field in cls.__dict__:
                fields[field] = cls.__dict__[field]
            else:
                fields[field] = None
        
        return fields

    def __new__(cls, arg):
        cls.fields = cls._init_fields(arg)
        cls.decorate(cls, arg)
        return arg
    
    @abstractmethod
    def decorate(cls, arg):
        pass