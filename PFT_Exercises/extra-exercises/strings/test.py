import unittest


import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise


class TestExercise(unittest.TestCase):
    """Tests for the exercise"""

    def test_utf16_to_str(self):
        self.assertEqual(exercise.utf16_to_str(
            b'\xff\xfe\xe5\x00\xe4\x00\xf6\x00p\x00l\x00o\x00k\x00'), "åäöplok")

    def test_str_to_utf8(self):
        self.assertEqual(exercise.str_to_utf8("åäöplok"),
                         b'\xc3\xa5\xc3\xa4\xc3\xb6plok')

    def test_hello_something(self):
        self.assertEqual(exercise.hello_something("me"), 'Hello me')
        self.assertEqual(exercise.hello_something(6), 'Hello 6')


unittest.main()
