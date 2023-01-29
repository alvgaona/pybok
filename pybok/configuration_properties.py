from inspect import isclass
import os
from typing import Any
from pybok.base_decorator import BaseDecorator
from pybok.decorators import _constructor


class ConfigurationProperties(BaseDecorator):
    def __init__(self, cls) -> None:
        super().__init__(cls)
    
    def __call__(self, *args, **kwargs) -> Any:
        self.decorate()

        if not isclass(self.cls) and self.cls.decorator:
            return self.cls(*args, **kwargs)
        else:
            return self.decorated_class(**self.fields)
    
    def decorate(self):
        _constructor(self.decorated_class, self.fields)

        for field in self.fields.keys():
            value = os.getenv(field.upper())
            if value is None and field in self.decorated_class.__dict__:
                self.fields[field] = self.decorated_class.__dict__[field]
            elif field not in self.decorated_class.__dict__ and value is None:
                raise ValueError(f"{field.upper()} is required.")
            else:        
                self.fields[field] = value