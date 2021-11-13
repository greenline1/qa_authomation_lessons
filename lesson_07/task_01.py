import unittest
from lesson_03.task_03 import is_year_leap
from lesson_03.task_04 import is_triangle, find_triangle_type
from lesson_05.task_01 import ITEmployee



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

    def test_triangle_04(self):
        sides = ('a', 'b', 'c')
        self.assertFalse(is_triangle(*sides))

    def test_triangle_type_01(self):
        sides = (3, 4, 5)
        self.assertEqual(find_triangle_type(*sides), "Versatile triangle")

    def test_triangle_type_02(self):
        sides = (5, 5, 5)
        self.assertEqual(find_triangle_type(*sides), "Equilateral triangle")

    def test_triangle_type_03(self):
        sides = (5, 5, 3)
        self.assertEqual(find_triangle_type(*sides), "Isosceles triangle")

    def test_triangle_type_04(self):
        sides = (0, 0, 0)
        self.assertEqual(find_triangle_type(*sides), "Not a triangle")

    def test_triangle_type_05(self):
        sides = ("a", "b", "c")
        self.assertEqual(find_triangle_type(*sides), "Not a triangle")


class TestLesson05(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("Jack Sparrow")

    def test_name(self):
        self.assertEqual(self.emp.fullname, "Jack Sparrow")

    def test_no_position(self):
        self.assertIsNone(self.emp.position)

    def test_no_skills(self):
        self.assertEqual(len(self.emp.skills), 0)

    def test_add_one_skill(self):
        self.emp.add_skill(['git'])
        self.assertIn('git', self.emp.skills)


if __name__ == '__main__':
    unittest.main()
