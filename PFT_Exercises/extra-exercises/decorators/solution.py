"""Create a decorator named 'logged' that decorates a function 
and logs name, arguments and return value using 'print()'
Tip: A function object has a member called __name__"""


def logged(fn):
    """Logs function calls to stdout
    Example::
      >>> @logged
      ... def fn(argument):
      ...    return "Having an %s" % (argument,)
      >>> fn("awful time")
      fn called with arguments: ('awful time',) {} 
          Returning Having an awful time
      'Having an awful time'
      >>> 
    """
    def wrapped(*args, **kwargs):
        retval = fn(*args, **kwargs)
        log_tpl = "%s called with arguments: %s %s \n\tReturning %s"
        print(log_tpl % (fn.__name__,
                         args,
                         kwargs,
                         retval))
        return retval
    return wrapped
