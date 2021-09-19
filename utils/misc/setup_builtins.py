import logging


def set_scope(variables: tuple[tuple, tuple]):
    """Add new variables to builtins scope.

    The variables argument is tuple or list that containing tuples or lists with a new variable name and variable value.

    `set_scope(variables=((variable_name, variables_value),))`

    :param variables:
    :return:
    """
    import builtins

    for variable in variables:
        if variable[0] not in builtins.__dict__:
            try:
                builtins.__dict__[variable[0]] = variable[1]
            except (KeyError, ValueError, TypeError):
                logging.exception(
                    f'Failed to set name ({variable[0]}) with value ({repr(variable[1])}) to builtins scope')
                continue
            else:
                logging.warning(
                    f'Successfully set  new name ({variable[0]}) with value ({repr(variable[1])}) to builtins scope')
        else:
            raise ValueError('A variable with the given name already exists in builtins scope')
