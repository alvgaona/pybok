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

def _constructor(cls, required_fields={}, default_fields={}, private=True):
    setattr(cls, f'__init__', _init_fn(required_fields, default_fields, private=private))
