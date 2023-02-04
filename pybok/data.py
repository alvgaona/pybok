from pybok.base import Base
from pybok.decorators import _init_fn, _getter_fn, _to_string_fn, _eq_fn, _hash_fn, _setter_fn


class Data(Base):
    def decorate(cls, arg):
        required_args = {}
        default_args = {}
        for field, value in cls.fields.items():
            if value is None:
                required_args[field] = value
            else:
                default_args[field] = value

        setattr(
            arg,
            '__init__',
            _init_fn(
                arg,
                required=required_args,
                default=default_args,
                private=True
            )
        )

        for field in cls.fields:
            setattr(arg, f'get_{field}', _getter_fn(field))
            setattr(arg, f'set_{field}', _setter_fn(field))

        setattr(arg, '__repr__', _to_string_fn(cls.fields))

        setattr(arg, '__eq__', _eq_fn())
        setattr(arg, '__hash__', _hash_fn(cls.fields))
