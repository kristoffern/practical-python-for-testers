import doctest

import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise

doctest.testmod(exercise, optionflags=doctest.NORMALIZE_WHITESPACE)
