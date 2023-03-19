from src.domain.Grade import Grade
from src.repository.GradeRepository import GradeRepository
from src.tests.Validations import RepositoryException

import unittest


class GradeRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__grade_repository = GradeRepository()

    def test_add_grade__adds_a_new_grade__the_grade_is_added_to_repository(self):
        self.__grade_repository.add_grade(Grade(1, "1", "1", 10))
        self.assertEqual(self.__grade_repository.get_grade(1), 10)

    def test_remove_grade__removes_a_grade__the_grade_is_removed_from_repository(self):
        self.__grade_repository.add_grade(Grade(1, "1", "1", 10))
        self.__grade_repository.remove_grade_by_id(1)
        self.assertEqual(len(self.__grade_repository), 0)

    def test_update_grade__updates_a_grade__with_new_information__the_grade_is_updated_correctly(self):
        self.__grade_repository.add_grade(Grade(1, "1", "1", 10))
        self.__grade_repository.update_grade(1, Grade(1, "1", "1", 9))
        self.assertEqual(self.__grade_repository.get_grade(1), 9)

    def test_remove_grade__removes_a_grade_that_not_exist__display_repository_exception(self):
        with self.assertRaises(RepositoryException) as error:
            self.__grade_repository.remove_grade_by_id(1)
        self.assertEqual(str(error.exception), "Grade with id:" + str(1) + "does not exist.")
