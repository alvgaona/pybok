from pybok.base import Base
from pybok.decorators import _create_fn


def _with_fn(fields, field):
    args = ",".join([f'{f}=self._{f}' for f in fields if f != field])
    return _create_fn(
        f'with_{field}',
        f'self, {field}',
        f'    return self if self._{field} == {field} else self.__class__({field}={field},{args})'
    )


class With(Base):
    def decorate(cls, arg):
        for field in cls.fields:
            setattr(arg, f'with_{field}', _with_fn(cls.fields, field))
