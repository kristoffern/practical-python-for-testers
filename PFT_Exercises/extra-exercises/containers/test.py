import unittest

import sys
if "solution" in sys.argv:
    import solution as exercise
    del sys.argv[sys.argv.index("solution")]
else:
    import exercise


class TestExercise(unittest.TestCase):
    """Tests for the exercise"""

    def test_add_to_list(self):

        the_list = [1, 2, 3, 4, 5, "string", []]
        original = list(the_list)

        # Don't add existing
        self.assertEqual(exercise.add_to_list(the_list, 3), original)

        # Add non-existing
        self.assertEqual(exercise.add_to_list(
            list(the_list), "3"), original + ["3"])
        self.assertEqual(exercise.add_to_list(
            list(the_list), "value"), original + ["value"])

    def test_remove_non_integers(self):

        the_dict = {1: 1, 2: "two", 3: 3}
        self.assertEqual(exercise.remove_non_integers(the_dict), {1: 1, 3: 3})

    def test_all_in_set(self):
        the_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.assertTrue(exercise.all_in_set(the_set, [1, 4, 7]))
        self.assertFalse(exercise.all_in_set(the_set, ["hej", 1, 3, 5, 6]))
        self.assertFalse(exercise.all_in_set(the_set, [10, 11, 135]))


unittest.main()
