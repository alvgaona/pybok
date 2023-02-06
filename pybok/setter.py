from pybok.base import Base
from pybok.property import Property


class Setter(Base):
    def decorate(cls, arg):
        for field in cls.fields:
            if field in arg.__dict__ and isinstance(arg.__dict__[field], Property):
                arg.__dict__[field].setter = True
            else:
                setattr(arg, field, Property(False, True))
                arg.__dict__[field].__set_name__(field)
