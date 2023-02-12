import inspect
from abc import ABC


def _create_fn(name, args, body, *, return_type=None, decorators=[], locals={}, globals={}):
    if args is None:
        args = ''

    decorators = '\n'.join(decorators)

    if decorators:
        decorators += '\n  '

    fn_txt = f'\n  {decorators}def {name}({args}) -> {return_type}: \n{body}'
    txt = f'def __create_fn__():{fn_txt}\n  return {name}'

    ns = {}

    if locals != {}:
        ns |= locals

    exec(txt, globals, ns)

    return ns['__create_fn__']()


def _no_args_init_fn(fields, private=False):
    body = []
    for f, v in fields.items():
        if private:
            body.append(f'self._{f} = {v}')
        else:
            body.append(f'self.{f} = {v}')
    body_txt = "\n".join(f'    {b}' for b in body)

    local_vars = 'self'

    return _create_fn('__init__', local_vars, body_txt)


def _no_init_fn():
    return _create_fn(
        '__init__',
        'self, *args, **kwargs',
        '\n    raise NotImplementedError("This is a utility class and cannot be instantiated")'
    )


def get_required_default_arguments(args):
    required = {}
    default = {}
    for field, value in args.items():
        if value is None:
            required[field] = value
        else:
            default[field] = value

    return required, default


def _init_fn(cls, required, default={}, super_args={}, private=False):
    super_class = inspect.getmro(cls)[1]
    super_base = super_class.__base__
    super_init_signature = inspect.signature(super_class.__init__)

    super_init_args = ",".join([f"{k}={k}" for k in super_args])
    if (super_base == ABC or str(super_init_signature) == '(self, /, *args, **kwargs)'):
        super_init_args = ""
    """
    HACK: the next line is just crazy. Needed to get the right class for the
    super method.

    The following lines are just standard.
    """
    body_txt = '    this = None\n    for klass in self.__class__.__mro__:\n   ' + \
        f'     if klass.__name__ == "{cls.__name__}":\n            this = klass\n'
    body_txt += f'    super(this, self).__init__({super_init_args})\n'

    body = []
    for f in list(required.keys()) + list(default.keys()):
        if private:
            body.append(f'self._{f} = {f}')
        else:
            body.append(f'self.{f} = {f}')

    body_txt += "\n".join(f'    {b}' for b in body)

    if super_init_args == "" and super_args != {}:
        for f in super_args:
            body_txt += f'\n    self._{f} = {f}'

    local_vars = 'self'
    super_required, super_default = get_required_default_arguments(super_args)

    for k, v in required.items():
        local_vars += f', {k}'

    for k, v in super_required.items():
        local_vars += f', {k}'

    if default or super_default:
        local_vars += ', *'

    for k, v in default.items():
        if isinstance(v, str):
            local_vars += f', {k}="{v}"'
        else:
            local_vars += f', {k}={v}'

    for k, v in super_default.items():
        if isinstance(v, str):
            local_vars += f', {k}="{v}"'
        else:
            local_vars += f', {k}={v}'

    return _create_fn('__init__', local_vars, body_txt)


def _getter_fn(field):
    return _create_fn(f'{field}', 'self', f'    return self._{field}', decorators=['@property'])


def _to_string_fn(fields):
    args = '+ ","'.join([f'"{name}=" + str(self._{name})' for name in fields])
    return _create_fn('__repr__', 'self', f'    return type(self).__name__ + "(" + {args} + ")"')


def _eq_fn():
    return _create_fn(
        '__eq__',
        'self, other',
        '    return self.__class__ == other.__class__ ' + 'and self.__dict__ == other.__dict__'
    )


def _hash_fn(fields):
    args = ','.join([f'self._{name}' for name in fields])
    return _create_fn('__hash__', 'self', f'    return hash(({args}))')
