from pybok.base_decorator import BaseDecorator
from pybok.decorators import _setter_fn

class Setter(BaseDecorator):
    def __init__(self, cls) -> None:
        super().__init__(cls)
    
    def decorate(self):
        for field in self.fields:
            setattr(self.decorated_class, f'set_{field}', _setter_fn(field))