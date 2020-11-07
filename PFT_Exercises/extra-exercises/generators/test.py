import unittest
from random import randrange

import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise


def dummy(): yield 1  # easy fetching of generator class


class TestExercise(unittest.TestCase):
    def test_infinite(self):

        for i in range(10):
            size = randrange(100, 10000)
            start = randrange(1, 1000000)
            inf = exercise.infinite(start)
            self.assertEqual(type(inf), type(dummy()), 'Not a generator')
            count = 0
            for i in inf:
                self.assertEqual(start+count, i)
                count += 1
                if count > size:
                    return


unittest.main()
