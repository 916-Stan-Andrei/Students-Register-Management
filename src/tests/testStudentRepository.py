from src.domain.Student import Student
from src.repository.StudentRepository import StudentRepository
from src.tests.Validations import RepositoryException

import unittest


class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__student_repository = StudentRepository()

    def test_add_student__adds_a_new_student__the_student_is_added_to_repository(self):
        self.__student_repository.add_student(Student("1", "John"))
        self.assertEqual(self.__student_repository.get_student("1"), "John")

    def test_remove_student__removes_a_student__the_student_is_removed_from_the_repository(self):
        self.__student_repository.add_student(Student("1", "John"))
        self.__student_repository.remove_student_by_id("1")
        self.assertEqual(len(self.__student_repository), 0)

    def test_update_student__updates_a_student_with_new_information__the_student_is_updated_correctly(self):
        self.__student_repository.add_student(Student("1", "John"))
        self.__student_repository.update_student("1", "Fred")
        self.assertEqual(self.__student_repository.get_student("1"), "Fred")

    def test_add_student__adds_a_student_with_the_same_id__display_repository_exception(self):
        self.__student_repository.add_student(Student("1", "John"))
        with self.assertRaises(RepositoryException) as error:
            self.__student_repository.add_student(Student("1", "John"))
        self.assertEqual(str(error.exception), "Student with id:" + str(1) + "already in repository!")