from src.tests.Validations import RepositoryException


class DisciplineRepository:
    def __init__(self):
        self.__data = dict()

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def add_discipline(self, discipline):
        if discipline.id in self.__data:
            raise RepositoryException("Discipline with id:" + str(discipline.id) + "already in repository!")
        self.__data[discipline.id] = discipline

    def remove_discipline_by_id(self, discipline_id):
        if discipline_id not in self.__data:
            raise RepositoryException("Discipline with id:" + str(discipline_id) + "does not exist")
        self.__data.pop(discipline_id)

    def update_discipline(self, discipline_id, discipline):
        if discipline_id not in self.__data:
            raise RepositoryException("Discipline with id:" + str(discipline_id) + "does not exist")
        self.__data[discipline_id].name = discipline

    def get_discipline(self, discipline_id):
        return self.__data[discipline_id].name

    def get_all(self):
        return list(self.__data.values())
