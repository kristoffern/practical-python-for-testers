"""This module pretends to do stuff"""


def do_stuff(stuff):
    """Prints that its doing stuff
    Example::

      >>> do_stuff('something')
      Doing something
      >>> do_stuff('1')
      Doing 1
    """
    print("Doing %s" % (stuff,))


def add(x, y):
    """Adds the float values of two arguments
    and returns the result::

      >>> add(1,2)
      3.0
      >>> add(0.5,2)
      2.5
      >>> add("5", 0)
      5.0
    """
    return float(x) + float(y)
