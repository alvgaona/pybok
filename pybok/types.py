from typing import Generic, TypeVar


T = TypeVar('T')


class Final(Generic[T]):
    pass


class Required(Generic[T]):
    pass


class NonNull(Generic[T]):
    pass
