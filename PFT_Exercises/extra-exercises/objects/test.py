import unittest
import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise


class TestExercise(unittest.TestCase):
    """Tests for the exercise"""

    def test_create_counter(self):
        exercise.Counter()

    def test_counter_add(self):
        c = exercise.Counter()
        c.add()

    def test_counter_remove(self):
        c = exercise.Counter()
        c.remove()

    def test_counter_value(self):
        c = exercise.Counter()
        c.remove()
        c.remove()
        c.add()
        self.assertEqual(c.value(), -1)


unittest.main()
