from src.tests.Validations import DomainException


class Student:
    def __init__(self, student_id, student_name):
        if not student_id.isnumeric():
            raise DomainException("The id should be numeric")
        if int(student_id) < 1:
            raise DomainException("The id should be greater than 0")
        self.__student_id = student_id
        self.__student_name = student_name

    @property
    def id(self):
        return self.__student_id

    @id.setter
    def id(self, value):
        self.__student_id = value

    @property
    def name(self):
        return self.__student_name

    @name.setter
    def name(self, value):
        self.__student_name = value

    def __str__(self):
        return str(self.id) + " " + str(self.name)
