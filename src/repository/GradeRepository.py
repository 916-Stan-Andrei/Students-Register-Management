from src.tests.Validations import RepositoryException


class GradeRepository:
    def __init__(self):
        self.__data = dict()

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def add_grade(self, grade):
        self.__data[grade.id] = grade

    def remove_grade_by_id(self, grade_id):
        if grade_id not in self.__data:
            raise RepositoryException("Grade with id:" + str(grade_id) + "does not exist.")
        self.__data.pop(grade_id)

    def update_grade(self, grade_id, grade):
        if grade_id not in self.__data:
            raise RepositoryException("Grade with id:" + str(grade_id) + "does not exist.")
        self.__data[grade_id] = grade

    def get_grade(self, grade_id):
        return self.__data[grade_id].grade_value

    def get_all(self):
        return list(self.__data.values())
