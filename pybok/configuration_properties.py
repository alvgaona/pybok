import os
from typing import Generic, TypeVar

from pybok.base import Base
from pybok.decorators import _init_fn


T = TypeVar('T')


class NotBlank(Generic[T]):
    pass


class ConfigurationProperties(Base):
    def decorate(cls, arg):
        for field in cls.fields.keys():
            value = os.getenv(field.upper())
            if value is None and field in arg.__dict__:
                cls.fields[field] = arg.__dict__[field]
            elif field not in arg.__dict__ and value is None:
                raise ValueError(f"{field.upper()} is required.")
            else:
                cls.fields[field] = value

        setattr(
            arg, '__init__', _init_fn(arg, required={}, default=cls.fields, super_args=cls.super_fields, private=True)
        )
