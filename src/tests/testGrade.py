import unittest

from src.domain.Grade import Grade
from src.tests.Validations import DomainException


class GradeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__grade = Grade(1, "3223", "1", 10)

    def test_init__creating_a_grade__allocates_the_grade_id_correctly(self):
        self.assertEqual(self.__grade.id, 1)

    def test_init__creating_a_grade__allocates_the_student_id_correctly(self):
        self.assertEqual(self.__grade.student_id, "3223")

    def test_init__creating_a_grade__allocates_the_discipline_id_correctly(self):
        self.assertEqual(self.__grade.discipline_id, "1")

    def test_init__creating_a_grade__allocates_the_grade_value_correctly(self):
        self.assertEqual(self.__grade.grade_value, 10)

    def test_setter__set_a_student_id__sets_the_value_correctly(self):
        self.__grade.student_id = "12"
        self.assertEqual(self.__grade.student_id, "12")

    def test_setter__set_a_discipline_id__sets_the_value_correctly(self):
        self.__grade.discipline_id = "123"
        self.assertEqual(self.__grade.discipline_id, "123")

    def test_init__giving_a_wrong_student_id__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Grade(1, "abc", "23", 10)
        self.assertEqual(str(error.exception), "The student id should be numeric")

    def test_init__giving_a_wrong_discipline_id__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Grade(1, "23", "abc", 10)
        self. assertEqual(str(error.exception), "The discipline id should be numeric")