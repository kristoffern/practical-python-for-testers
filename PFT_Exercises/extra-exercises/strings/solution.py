"""Remember, bytes are encoded strings"""


def utf16_to_str(data):
    """Convert the given byte data to a string using utf-16"""
    return data.decode("utf-16")


def str_to_utf8(string):
    """Convert the given string to a bytes object using utf-8"""
    return string.encode("utf-8")


def hello_something(something):
    """Return a 'Hello <something>' string for a given value
    of something. """
    return "Hello %s" % (something,)
