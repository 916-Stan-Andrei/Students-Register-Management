import unittest

from src.domain.Discipline import Discipline
from src.tests.Validations import DomainException


class DisciplineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__discipline = Discipline("123", "Mathematics")

    def test_discipline__creating_a_discipline__allocates_the_id_correctly(self):
        self.assertEqual(self.__discipline.id, "123")

    def test_discipline__creating_a_discipline__allocates_the_name_correctly(self):
        self.assertEqual(self.__discipline.name, "Mathematics")

    def test_setter__set_an_id_for_a_discipline__sets_the_value_correctly(self):
        self.__discipline.id = "123"
        self.assertEqual(self.__discipline.id, "123")

    def test_setter__set_a_name_for_a_discipline__sets_the_name_correctly(self):
        self.__discipline.name = "Math"
        self.assertEqual(self.__discipline.name, "Math")

    def test_init__giving_a_wrong_id__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Discipline("Wrong Id", "Math")
        self.assertEqual(str(error.exception), "The id should be numeric")

    def test_init__giving_an_id_smaller_than_1__display_the_correct_error(self):
        with self.assertRaises(DomainException) as error:
            Discipline("0", "FP")
        self.assertEqual(str(error.exception), "The id should be greater than 0")

