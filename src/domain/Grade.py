from src.tests.Validations import DomainException


class Grade:
    def __init__(self, grade_id, student_id, discipline_id, grade_value):
        if not student_id.isnumeric():
            raise DomainException("The student id should be numeric")
        if not discipline_id.isnumeric():
            raise DomainException("The discipline id should be numeric")
        if int(student_id) < 1 or int(discipline_id) < 1:
            raise DomainException("The id should be greater than 0")
        if int(grade_value) < 1 or int(grade_value) > 10:
            raise DomainException("The grade should be [1,10]")
        self.__grade_id = grade_id
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value

    @property
    def id(self):
        return self.__grade_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, value):
        self.__discipline_id = value

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, value):
        self.__grade_value = value

    def __str__(self):
        return str(self.student_id) + " " + str(self.discipline_id) + " " + str(self.grade_value)
