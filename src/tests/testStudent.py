import unittest

from src.domain.Student import Student
from src.tests.Validations import DomainException


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__student = Student("123", "John")

    def test_student__creating_a_student__allocates_the_id_correctly(self):
        self.assertEqual(self.__student.id, "123")

    def test_student__creating_a_student__allocates_the_name_correctly(self):
        self.assertEqual(self.__student.name, "John")

    def test_init__check_if_id_has_only_digits__the_id_should_be_correct(self):
        self.assertEqual(self.__student.id, "123")

    def test_setter__set_an_id_for_a_student__sets_the_value_correctly(self):
        self.__student.id = "123"
        self.assertEqual(self.__student.id, "123")

    def test_setter__set_a_name_for_a_student__sets_the_name_correctly(self):
        self.__student.name = "Math"
        self.assertEqual(self.__student.name, "Math")

    def test_init__giving_a_wrong_id__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Student("Wrong Id", "John")
        self.assertEqual(str(error.exception), "The id should be numeric")

    def test_init__giving_an_id_smaller_than_1__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Student("0", "John")
        self.assertEqual(str(error.exception), "The id should be greater than 0")
