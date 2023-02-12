from pybok.base import Base
from pybok.decorators import _init_fn, get_required_default_arguments


class ArgsConstructor(Base):
    def decorate(cls, arg):
        required, default = get_required_default_arguments(cls.fields)
        setattr(
            arg,
            '__init__',
            _init_fn(arg, required=required, default=default, super_args=cls.super_fields, private=True)
        )
