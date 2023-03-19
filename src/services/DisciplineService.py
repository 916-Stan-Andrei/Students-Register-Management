from src.domain.Discipline import Discipline
from src.repository.DisciplineRepository import DisciplineRepository


class DisciplineService:
    def __init__(self):
        self.__discipline_repository = DisciplineRepository()

    def __len__(self):
        return self.__discipline_repository.__len__()

    def add_discipline(self, discipline_id, discipline_name):
        new_discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.add_discipline(new_discipline)

    def remove_discipline(self, discipline_id):
        self.__discipline_repository.remove_discipline_by_id(discipline_id)

    def update_discipline(self, discipline_id, discipline_name):
        self.__discipline_repository.update_discipline(discipline_id, discipline_name)

    def search_by_id_in_list_of_disciplines(self, searched_argument):
        list_of_matched_disciplines = list()
        for discipline in self.get_all():
            if searched_argument == str(discipline.id):
                list_of_matched_disciplines.append(discipline)
        return list_of_matched_disciplines

    def search_by_name_in_list_of_disciplines(self, searched_argument):
        list_of_matched_disciplines = list()
        for discipline in self.get_all():
            if searched_argument.lower() in str(discipline.name).lower():
                list_of_matched_disciplines.append(discipline)
        return list_of_matched_disciplines

    def get_discipline(self, discipline_id):
        return self.__discipline_repository.get_discipline(discipline_id)

    def get_all(self):
        return self.__discipline_repository.get_all()
