from src.services.StudentService import StudentService

import unittest


class StudentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__student_service = StudentService()

    def test_add_student__adds_a_new_student__should_add_a_new_student_to_repository(self):
        self.__student_service.add_student("1", "Marius")
        self.assertEqual(self.__student_service.get_student("1"), "Marius")

    def test_remove_student__removes_an_existing_student__should_remove_without_errors(self):
        self.__student_service.add_student("1", "Marius")
        self.__student_service.remove_student("1")
        self.assertEqual(len(self.__student_service), 0)

    def test_update_student__update_an_existing_student_with_a_new_name__should_update_without_errors(self):
        self.__student_service.add_student("1", "Marius")
        self.__student_service.update_student("1", "Darius")
        self.assertEqual(self.__student_service.get_student("1"), "Darius")

