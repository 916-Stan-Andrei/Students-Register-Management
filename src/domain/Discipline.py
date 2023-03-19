from src.tests.Validations import DomainException


class Discipline:
    def __init__(self, discipline_id, discipline_name):
        if not discipline_id.isnumeric():
            raise DomainException("The id should be numeric")
        if int(discipline_id) < 1:
            raise DomainException("The id should be greater than 0")
        self.__discipline_id = discipline_id
        self.__discipline_name = discipline_name

    @property
    def id(self):
        return self.__discipline_id

    @id.setter
    def id(self, value):
        self.__discipline_id = value

    @property
    def name(self):
        return self.__discipline_name

    @name.setter
    def name(self, value):
        self.__discipline_name = value

    def __str__(self):
        return str(self.id) + " " + str(self.name)
