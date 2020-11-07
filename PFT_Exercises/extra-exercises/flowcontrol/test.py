import unittest

import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise


class TestExercise(unittest.TestCase):
    """Tests for the exercise"""

    def test_count(self):
        self.assertEqual(exercise.count_above(range(10), 5), 4)

    def test_add(self):
        self.assertEqual(exercise.add_all(
            ["3"] + list(range(10)) + ["k", {}, []]), 45)

    def test_count_below(self):
        self.assertEqual(exercise.count_below(range(10), 5), 5)

    def test_count_below_default(self):
        self.assertEqual(exercise.count_below(range(10)), 5)


unittest.main()
