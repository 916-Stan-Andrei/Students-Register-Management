from src.services.GradeService import GradeService
from src.domain.Grade import Grade

import unittest


class GradeServiceTest (unittest.TestCase):
    def setUp(self) -> None:
        self.__grade_service = GradeService()

    def test_add_grade__adds_a_new_grade__should_add_a_new_grade_to_service_repository(self):
        self.__grade_service.add_grade("1", "1", 10)
        self.assertEqual(self.__grade_service.get_grade(1), 10)

    def test_remove_grade__removes_a_grade_that_already_exists__should_delete_a_grade_with_no_errors(self):
        self.__grade_service.add_grade("1", "1", 10)
        self.__grade_service.remove_grade(1)
        self.assertEqual(len(self.__grade_service), 0)

    def test_update_grade__updates_a_grade_that_already_exists_with_a_new_one__should_update_the_grade_with_no_errors(self):
        self.__grade_service.add_grade("1", "1", 10)
        self.__grade_service.update_grade(1, Grade(1, "1", "1", 9))
        self.assertEqual(self.__grade_service.get_grade(1), 9)

