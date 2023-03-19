from src.services.StudentService import StudentService
from src.services.DisciplineService import DisciplineService
from src.services.GradeService import GradeService
from src.tests.Validations import RepositoryException
from src.tests.Validations import DomainException
from src.services.UndoService import UndoService
from src.tests.Validations import UndoException
from src.domain.Student import Student
from src.domain.Discipline import Discipline
from src.domain.Grade import Grade

import traceback
import random


class UserInterface:
    def __init__(self):
        self.__student_service = StudentService()
        self.__discipline_service = DisciplineService()
        self.__grade_service = GradeService()
        self.__undo_service = UndoService(self.__student_service, self.__discipline_service, self.__grade_service)
        self.__options = {
            "list": self.list,
            "add": self.ui_add,
            "remove": self.ui_remove,
            "update": self.ui_update,
            "search": self.ui_search,
            "failing students": self.ui_all_students_failing_at_one_or_more_disciplines,
            "top students": self.ui_top_students,
            "best disciplines": self.ui_disciplines_with_best_grades,
            "menu": self.display_menu
        }

    @staticmethod
    def display_menu():
        print("\nadd: add an object")
        print("remove: delete an object")
        print("update: update an object")
        print("list: display an object")
        print("search: search for an object")
        print("failing students: display all failing students")
        print("top students: display top students")
        print("best disciplines: display disciplines and their averages")
        print("menu: display the menu")
        print("x: exit the program\n")

    def populate(self):
        students = ["Marius", "Daniel", "Maria ", "Denisa", "John  "]
        disciplines = ["English    ", "Programming", "Mathematics", "Physics    "]
        for i in range(0, 5):
            self.__student_service.add_student(str(i+1), students[i])
        for i in range(0, 4):
            self.__discipline_service.add_discipline(str(i+1), disciplines[i])
        for i in range(1, 6):
            for j in range(1, 5):
                random_grade = random.randint(1, 10)
                self.__grade_service.add_grade(str(i), str(j), random_grade)

    def list(self):
        chosen_object = input("Enter the object:")
        print()
        try:
            if chosen_object == "student":
                list_of_students = self.__student_service.get_all()
                for student_information in list_of_students:
                    self.print_student_information(student_information)
            elif chosen_object == "discipline":
                list_of_disciplines = self.__discipline_service.get_all()
                for discipline_information in list_of_disciplines:
                    self.print_discipline_information(discipline_information)
            elif chosen_object == "grade":
                list_of_grades = self.__grade_service.get_all()
                for grade_information in list_of_grades:
                    self.print_grade_information(self.__student_service.get_student(grade_information.student_id), self.__discipline_service.get_discipline(grade_information.discipline_id), self.__grade_service.get_grade(grade_information.id))
            else:
                raise ValueError(f"The service {chosen_object} does not exist!")
        except DomainException:
            print("Domain Error")
        except RepositoryException:
            print("Repository error")

    def ui_add(self):
        chosen_object = input("Enter the object:")
        print()
        try:
            if chosen_object == "student":
                student_id = input("Give the id of the student:")
                student_name = input("Give the name of the student:")
                self.__student_service.add_student(str(student_id), student_name)
                self.__undo_service.add_command_to_stack("add_student", Student(student_id, student_name))
            elif chosen_object == "discipline":
                discipline_id = input("Give the id of the discipline:")
                discipline_name = input("Give the name of the discipline:")
                self.__discipline_service.add_discipline(str(discipline_id), discipline_name)
                self.__undo_service.add_command_to_stack("add_discipline", Discipline(discipline_id, discipline_name))
            elif chosen_object == "grade":
                student_id = input("Give the id of the student:")
                discipline_id = input("Give the id of the discipline:")
                grade = input("Give a grade:")
                self.__grade_service.add_grade(str(student_id), str(discipline_id), grade)
                self.__undo_service.add_command_to_stack("add_grade", Grade(self.__grade_service.get_id(), student_id, discipline_id, grade))
            else:
                raise ValueError(f"The service {chosen_object} does not exist!")
        except DomainException:
            print("error")
        except RepositoryException:
            print("error")

    def ui_remove(self):
        chosen_object = input("Enter the object:")
        print()
        try:
            if chosen_object == "student":
                student_id = input("Give the id of the student you want to remove:")
                copy_student_id = student_id
                copy_student_name = self.__student_service.get_student(str(student_id))
                self.__student_service.remove_student(str(student_id))
                for grade in self.__grade_service.get_all():
                    if str(grade.student_id) == str(student_id):
                        copy_grade_student_id = grade.student_id
                        copy_grade_discipline_id = grade.discipline_id
                        copy_grade_value = grade.grade_value
                        self.__grade_service.remove_grade(int(grade.id))
                        self.__undo_service.add_command_to_stack("remove_grade", Grade(grade.id, copy_grade_student_id, copy_grade_discipline_id, copy_grade_value))
                self.__undo_service.add_command_to_stack("remove_student", Student(copy_student_id, copy_student_name))
            elif chosen_object == "discipline":
                discipline_id = input("Give the id of the discipline you want to remove:")
                copy_discipline_id = discipline_id
                copy_discipline_name = self.__discipline_service.get_discipline(discipline_id)
                self.__discipline_service.remove_discipline(str(discipline_id))
                for grade in self.__grade_service.get_all():
                    if str(grade.discipline_id) == str(discipline_id):
                        copy_grade_student_id = grade.student_id
                        copy_grade_discipline_id = grade.discipline_id
                        copy_grade_value = grade.grade_value
                        self.__grade_service.remove_grade(int(grade.id))
                        self.__undo_service.add_command_to_stack("remove_grade", Grade(grade.id, copy_grade_student_id, copy_grade_discipline_id, copy_grade_value))
                self.__undo_service.add_command_to_stack("remove_discipline", Discipline(copy_discipline_id, copy_discipline_name))
            else:
                raise ValueError(f"The service {chosen_object} does not exist!")
        except DomainException:
            print("error")
        except RepositoryException:
            print("error")

    def ui_update(self):
        chosen_object = input("Enter the object:")
        print()
        try:
            if chosen_object == "student":
                student_id = input("Give the id of the student you want to update:")
                student_name = input("Give a new name for the student:")
                self.__undo_service.add_command_to_stack("update_student", Student(student_id, f"{self.__student_service.get_student(student_id)},{student_name}"))
                self.__student_service.update_student(student_id, student_name)
            elif chosen_object == "discipline":
                discipline_id = input("Give the id of the discipline you want to update:")
                discipline_name = input("Give a new discipline name:")
                self.__undo_service.add_command_to_stack("update_discipline", Discipline(discipline_id, f"{self.__discipline_service.get_discipline(discipline_id)},{discipline_name}"))
                self.__discipline_service.update_discipline(discipline_id, discipline_name)
            else:
                raise ValueError(f"The service {chosen_object} does not exist!")
        except DomainException:
            print("error")
        except RepositoryException:
            print("error")

    def ui_search(self):
        chosen_object = input("Enter the object:")
        print()
        try:
            if chosen_object == "student":
                object_type = input("Do you want to search based on id or name? ").strip().lower()
                if object_type == "id":
                    searched_argument = input("Give an id:")
                    list_of_matched_students = self.__student_service.search_by_id_in_list_of_students(searched_argument)
                    for student in list_of_matched_students:
                        self.print_student_information(student)
                elif object_type == "name":
                    searched_argument = input("Give a name:")
                    list_of_matched_students = self.__student_service.search_by_name_in_list_of_students(searched_argument)
                    for student in list_of_matched_students:
                        self.print_student_information(student)
            elif chosen_object == "discipline":
                object_type = input("Do you want to search based on id or name? ").strip().lower()
                if object_type == "id":
                    searched_argument = input("Give an id:")
                    list_of_matched_disciplines = self.__discipline_service.search_by_id_in_list_of_disciplines(searched_argument)
                    for discipline in list_of_matched_disciplines:
                        self.print_discipline_information(discipline)
                elif object_type == "name":
                    searched_argument = input("Give a name:")
                    list_of_matched_disciplines = self.__discipline_service.search_by_name_in_list_of_disciplines(searched_argument)
                    for discipline in list_of_matched_disciplines:
                        self.print_discipline_information(discipline)
            else:
                raise ValueError(f"The service {chosen_object} does not exist!")
            print()
        except DomainException:
            print("error")
        except RepositoryException:
            print("error")

    def ui_all_students_failing_at_one_or_more_disciplines(self):
        list_of_failing_students = self.__grade_service.all_students_failing_at_one_or_more_disciplines(self.__student_service, self.__discipline_service)
        print()
        for i in list_of_failing_students:
            print(f"Student: {i[0].name}\t\t"
                  f"Discipline: {i[1].name}\t\t"
                  f"Average: {i[2]}")
        print()

    def ui_top_students(self):
        list_of_top_students = self.__grade_service.students_with_the_best_situation_in_descending_order(self.__student_service, self.__discipline_service)
        print()
        for i in list_of_top_students:
            print(f"Student: {i[0].name}\t\t"
                  f"Average: {i[1]}")

    def ui_disciplines_with_best_grades(self):
        list_of_disciplines = self.__grade_service.all_disciplines_sorted_by_average_grades_received_by_students(self.__student_service, self.__discipline_service)
        print()
        for i in list_of_disciplines:
            print(f"Discipline:{i[0].name}\t\t"
                  f"Average:{i[1]}")

    @staticmethod
    def print_student_information(student_information):
        print(f"ID:{student_information.id}\tName:{student_information.name}")

    @staticmethod
    def print_discipline_information(discipline_information):
        print(f"ID:{discipline_information.id}\tName:{discipline_information.name}")

    @staticmethod
    def print_grade_information(*grade_information):
        print(f"Name:{grade_information[0]}"
              f"\t\tDiscipline:{grade_information[1]}\t\t"
              f"Grade:{grade_information[2]}")

    def run_menu(self):
        self.populate()
        print()
        self.display_menu()
        while True:
            print()
            option = (input("Enter your option:")).strip()
            try:
                if option == "x":
                    return
                elif option == "undo":
                    self.__undo_service.call_undo()
                elif option == "redo":
                    self.__undo_service.call_redo()
                else:
                    self.__options[option]()
            except UndoException:
                print("Nothing to undo/redo")
            except ValueError:
                print("ValueError")
            except KeyError:
                print("KeyError")
                traceback.print_exc()










