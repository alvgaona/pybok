from pybok.base import Base
from pybok.decorators import _init_fn

class ArgsConstructor(Base):
    def decorate(cls, arg):
        required_args = {}
        default_args = {}
        for field, value in cls.fields.items():
            if value is None:
                required_args[field] = value
            else:
                default_args[field] = value

        setattr(arg, f'__init__', _init_fn(required_fields=required_args, default_fields=default_args, private=True))