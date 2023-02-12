import re
from inspect import Parameter, signature

from pybok.base import Base
from pybok.decorators import _create_fn, _no_args_init_fn


def _create_cls(name, parents=""):
    ns = {}
    exec(f'class {name}({parents}):\n    pass', None, ns)
    return ns[name]


def builder_class(name, fields):
    cls = _create_cls(f'{name}Builder')

    setattr(cls, '__init__', _no_args_init_fn(fields, private=True))

    for f in fields:
        fn = _create_fn(f, f'self, {f}', f'    self._{f} = {f}\n    return self', return_type='str')
        setattr(cls, f, fn)

    return cls


class Builder(Base):
    def decorate(cls, arg):
        setattr(arg, '_fields', {})

        builder_cls = builder_class(arg.__name__, cls.fields)

        def builder():
            return builder_cls()

        setattr(arg, 'builder', builder)

        def build(self):
            values = {re.sub('^_', '', k): v for k, v in self.__dict__.items()}
            print(signature(arg.__init__))
            parameters = signature(arg.__init__).parameters
            for k, v in values.items():
                kind = parameters[k].kind
                if (kind == Parameter.POSITIONAL_OR_KEYWORD or kind == Parameter.POSITIONAL_ONLY) and v is None:
                    raise TypeError(f"__init__() missing required positional argument: '{k}'")

            return arg(**values)

        setattr(builder_cls, 'build', build)
