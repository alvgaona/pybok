def _create_fn(name, args, body, *, return_type=None, decorators=[]):
    if args is None:
        args = ''

    decorators = '\n'.join(decorators)

    if decorators:
        decorators += '\n  '

    txt = f'def __create_fn__():\n  {decorators}def {name}({args}) -> {return_type}: \n{body}\n  return {name}'

    ns = {}
    exec(txt, None, ns)

    return ns['__create_fn__']()


def _no_args_init_fn(fields, private=False):
    body = []
    for f in fields:
        if private:
            body.append(f'self._{f} = None')
        else:
            body.append(f'self.{f} = None')
    body_txt = "\n".join(f'    {b}' for b in body)

    local_vars = 'self'

    return _create_fn('__init__', local_vars, body_txt)


def _no_init_fn():
    return _create_fn(
        '__init__',
        'self, *args, **kwargs',
        '\n    raise NotImplementedError("This is a utility class and cannot be instantiated")'
    )


def _init_fn(required_fields, default_fields={}, private=False):
    body = []
    for f in list(required_fields.keys()) + list(default_fields.keys()):
        if private:
            body.append(f'self._{f} = {f}')
        else:
            body.append(f'self.{f} = {f}')
    body_txt = "\n".join(f'    {b}' for b in body)

    local_vars = 'self'

    for k, v in required_fields.items():
        local_vars += f', {k}'

    for k, v in default_fields.items():
        if isinstance(v, str):
            local_vars += f', {k}="{v}"'
        else:
            local_vars += f', {k}={v}'

    return _create_fn('__init__', local_vars, body_txt)


def _getter_fn(field):
    return _create_fn(f'get_{field}', 'self', f'    return self._{field}')


def _setter_fn(field):
    return _create_fn(f'set_{field}', f'self, {field}', f'    self._{field} = {field}')


def _to_string_fn(fields):
    args = '+ ","'.join([f'"{name}=" + str(self._{name})' for name in fields])
    return _create_fn('__repr__', 'self', f'    return type(self).__name__ + "(" + {args} + ")"')


def _constructor(cls, required_fields={}, default_fields={}, private=True):
    setattr(cls, '__init__', _init_fn(required_fields, default_fields, private=private))


def _eq_fn():
    return _create_fn(
        '__eq__',
        'self, other',
        '    return self.__class__ == other.__class__ ' +
        'and self.__dict__ == other.__dict__'
    )


def _hash_fn(fields):
    args = ','.join([f'self._{name}' for name in fields])
    return _create_fn('__hash__', 'self', f'    return hash(({args}))')
