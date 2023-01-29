def _create_fn(name, args, body, *, return_type=None):
    if args is None:
        args = ''

    txt = f'def __create_fn__():\n  def {name}({args}) -> {return_type}: \n{body}\n  return {name}'
    
    ns = {}
    exec(txt, None, ns)

    return ns['__create_fn__']()

def _init_fn(fields):
    body = []
    for f in fields:
        body.append(f'self.{f} = {f}')
    body_txt = "\n".join(f'    {b}' for b in body)

    local_vars = 'self'
    for k, v in fields.items():
        if v is None:
            local_vars += f', {k}'
        else:
            local_vars += f', {k}={v}'

    return _create_fn('__init__', local_vars, body_txt)

def _getter_fn(field):
    return _create_fn(f'get_{field}', 'self', f'    return self.{field}')

def _setter_fn(field):
    return _create_fn(f'set_{field}', f'self, {field}', f'    self.{field} = {field}')

def _constructor(cls, fields):
    setattr(cls, f'__init__', _init_fn(fields))
