from inspect import isclass
from typing import Any


class BaseDecorator:
    def __init__(self, cls) -> None:
        self.cls = cls
        if isclass(cls):
            self.decorated_class = cls
        else:
            self.decorated_class = cls.decorated_class 
        self.decorator = True
        
        self.fields = self._init_fields(cls)
    
    def __call__(self, *args, **kwargs) -> Any:
        self.decorate()

        if not isclass(self.cls) and self.cls.decorator:
            return self.cls(*args, **kwargs)
        else:
            return self.decorated_class(*args, **kwargs)

    def decorate(self):
        pass
        
    def _init_fields(self, cls):
        if isclass(cls):
            fields = {}

            for field in cls.__annotations__.keys():
                if field in cls.__dict__:
                    fields[field] = cls.__dict__[field]
                else:
                    fields[field] = None
            
            return fields
        else:
            return cls.fields