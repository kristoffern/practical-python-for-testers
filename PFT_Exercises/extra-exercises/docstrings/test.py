
import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise

import doctest

doctest.testmod(exercise)
