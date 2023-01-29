from pybok.base_decorator import BaseDecorator
from pybok.decorators import _constructor

class ArgsConstructor(BaseDecorator):
    def __init__(self, cls) -> None:
        super().__init__(cls)

    def decorate(self):
        _constructor(self.decorated_class, self.fields)