from pybok.base import Base


class Instances(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Instances, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseSingleton(metaclass=Instances):
    pass


class Singleton(Base):
    def __new__(cls, arg=None, *args, **kwargs):
        """
        NOTE: it's a redefinition of the method in the Base class.
        Please read the comment in the base method.
        """
        if arg is not None:
            cls.fields, cls.super_fields = cls._init_fields(arg)

            new_arg = type(arg.__name__, (BaseSingleton,), dict(arg.__dict__))
            cls.decorate(cls, new_arg)
            return new_arg
        else:
            cls.args = args
            cls.kwargs = kwargs
            return cls
