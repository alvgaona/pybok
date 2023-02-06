class Property:
    def __init__(self, getter=True, setter=True) -> None:
        self.getter = getter
        self.setter = setter

    def __set_name__(self, name):
        self.public_name = name
        self.private_name = '_' + name

    def __set__(self, obj, value):
        if self.setter is False:
            msg = f"Setter is not available for property '{self.public_name}'"
            raise TypeError(msg)

        setattr(obj, self.private_name, value)

    def __get__(self, obj, objtype=None):
        if self.getter is False:
            msg = f"Getter is not available for property '{self.public_name}'"
            raise TypeError(msg)

        value = getattr(obj, self.private_name)
        return value
