from src.domain.Discipline import Discipline
from src.repository.DisciplineRepository import DisciplineRepository
from src.tests.Validations import RepositoryException

import unittest


class DisciplineRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__discipline_repository = DisciplineRepository()

    def test_add_discipline__adds_a_new_discipline__the_discipline_is_added_to_repository(self):
        self.__discipline_repository.add_discipline(Discipline("1", "English"))
        self.assertEqual(self.__discipline_repository.get_discipline("1"), "English")

    def test_remove_discipline__removes_a_discipline__the_discipline_is_removed_from_the_repository(self):
        self.__discipline_repository.add_discipline(Discipline("1", "English"))
        self.__discipline_repository.remove_discipline_by_id("1")
        self.assertEqual(len(self.__discipline_repository), 0)

    def test_update_discipline__updates_the_name_of_a_discipline_depending_on_id__the_discipline_is_updated_correctly(self):
        self.__discipline_repository.add_discipline(Discipline("1", "English"))
        self.__discipline_repository.update_discipline("1", "Math")
        self.assertEqual(self.__discipline_repository.get_discipline("1"), "Math")

    def test_add_discipline__adds_a_discipline_with_the_same_id__display_repository_exception(self):
        self.__discipline_repository.add_discipline(Discipline("1", "English"))
        with self.assertRaises(RepositoryException) as error:
            self.__discipline_repository.add_discipline(Discipline("1", "English"))
        self.assertEqual(str(error.exception), "Discipline with id:" + str(1) + "already in repository!")
