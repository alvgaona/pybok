from pybok.base import Base
from pybok.decorators import _create_fn


class Builder(Base):
    @classmethod
    def _builder_set(cls, name):
        body = f'    cls._fields["{name}"] = {name}\n    return cls'
        return _create_fn(name, 'cls, ' + name, body, decorators=['@classmethod'])
    

    def decorate(klass, arg):
        setattr(arg, '_fields', {})

        for field in klass.fields:
            setattr(arg, field, klass._builder_set(field))

        @classmethod
        def build(cls):
            return arg(**arg._fields)

        setattr(arg, 'build', build)
