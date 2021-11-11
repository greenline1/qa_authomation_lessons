import unittest
from lesson_03.task_03 import is_year_leap
from lesson_03.task_04 import is_triangle


class TestLesson03(unittest.TestCase):

    def test_leap_year_01(self):
        year = 2000
        self.assertTrue(is_year_leap(year))

    def test_leap_year_02(self):
        year = 2020
        self.assertTrue(is_year_leap(year))

    def test_leap_year_03(self):
        year = 1998
        self.assertFalse(is_year_leap(year))

    def test_triangle_01(self):
        sides = (3, 4, 5)
        self.assertTrue(is_triangle(*sides))

    def test_triangle_02(self):
        sides = (1, 2, 3)
        self.assertFalse(is_triangle(*sides))

    def test_triangle_03(self):
        sides = (0, 0, 0)
        self.assertFalse(is_triangle(*sides))


if __name__ == '__main__':
    unittest.main()
