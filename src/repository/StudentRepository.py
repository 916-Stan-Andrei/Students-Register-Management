from src.tests.Validations import RepositoryException


class StudentRepository:
    def __init__(self):
        self.__data = dict()

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def add_student(self, student):
        if student.id in self.__data:
            raise RepositoryException("Student with id:" + str(student.id) + "already in repository!")
        self.__data[student.id] = student

    def remove_student_by_id(self, student_id):
        if student_id not in self.__data:
            raise RepositoryException("Student with id:" + str(student_id) + "does not exist")
        self.__data.pop(student_id)

    def update_student(self, student_id, student):
        if student_id not in self.__data:
            raise RepositoryException("Student with id:" + str(student_id) + "does not exist")
        self.__data[student_id].name = student

    def get_student(self, student_id):
        return self.__data[student_id].name

    def get_all(self):
        return list(self.__data.values())
