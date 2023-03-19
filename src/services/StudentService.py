from src.domain.Student import Student
from src.repository.StudentRepository import StudentRepository


class StudentService:
    def __init__(self):
        self.__student_repository = StudentRepository()

    def __len__(self):
        return self.__student_repository.__len__()

    def __getitem__(self, item):
        return self.__student_repository[item]

    def add_student(self, student_id, student_name):
        new_student = Student(student_id, student_name)
        self.__student_repository.add_student(new_student)

    def remove_student(self, student_id):
        self.__student_repository.remove_student_by_id(student_id)

    def update_student(self, student_id, student_name):
        self.__student_repository.update_student(student_id, student_name)

    def search_by_id_in_list_of_students(self, searched_argument):
        list_of_matched_students = list()
        for student in self.get_all():
            if searched_argument in str(student.id):
                list_of_matched_students.append(student)
        return list_of_matched_students

    def search_by_name_in_list_of_students(self, searched_argument):
        list_of_matched_students = list()
        for student in self.get_all():
            if searched_argument.lower() in str(student.name).lower():
                list_of_matched_students.append(student)
        return list_of_matched_students

    def get_student(self, student_id):
        return self.__student_repository.get_student(student_id)

    def get_all(self):
        return self.__student_repository.get_all()
