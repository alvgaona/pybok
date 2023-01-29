from pybok.base_decorator import BaseDecorator
from pybok.decorators import _getter_fn

class Getter(BaseDecorator):
    def __init__(self, cls) -> None:
        super().__init__(cls)

    def decorate(self):
        for field in self.fields:
            setattr(self.decorated_class, f'get_{field}', _getter_fn(field))