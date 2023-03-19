from src.services.DisciplineService import DisciplineService

import unittest


class DisciplineServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__discipline_service = DisciplineService()

    def test_add_discipline__adds_a_discipline__should_add_discipline_to_service_repository(self):
        self.__discipline_service.add_discipline("1", "Math")
        self.assertEqual(self.__discipline_service.get_discipline("1"), "Math")

    def test_remove_discipline__removes_a_discipline__should_remove_discipline_from_service_repository(self):
        self.__discipline_service.add_discipline("1", "Math")
        self.__discipline_service.remove_discipline("1")
        self.assertEqual(len(self.__discipline_service), 0)

    def test_update_discipline__updates_a_discipline_with_new_information__should__update_a_discipline__from_service_repository(self):
        self.__discipline_service.add_discipline("1", "Math")
        self.__discipline_service.update_discipline("1", "English")
        self.assertEqual(self.__discipline_service.get_discipline("1"), "English")