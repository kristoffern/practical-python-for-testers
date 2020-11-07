import unittest
import sys


if "solution" in sys.argv:
    solution = True
    del sys.argv[sys.argv.index("solution")]
else:
    solution = False


class OutWrap(object):
    def __init__(self, wrapee):
        self.wrapee = wrapee
        self.count = 0
        self.msgs = []

    def write(self, *args, **kwargs):
        self.count += 1
        self.msgs.append(args)
        return self.wrapee.write(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.wrapee, name)


class TestExercise(unittest.TestCase):
    """Tests for the exercise"""

    def test_import(self):
        wrap = OutWrap(sys.stdout)
        sys.stdout = wrap

        if solution:
            import solution as exercise
        else:
            import exercise

        sys.stdout = wrap.wrapee
        print(wrap.msgs)
        self.assertEqual(
            wrap.count, 0, "Importing exercise printed to stdout!")
        self.assertEqual(exercise.get_message(), 'Hello World')


unittest.main()
