from src.tests.Validations import UndoException


class UndoService:
    def __init__(self, student_service, discipline_service, grade_service):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_service = grade_service
        self.__the_command_from_the_top_of_the_stack = -1
        self.__command_stack = list()
        self.__undo_dictionary = {
            "add_student": self.undo_add_student,
            "remove_student": self.undo_remove_student,
            "update_student": self.undo_update_student,
            "add_discipline": self.undo_add_discipline,
            "remove_discipline": self.undo_remove_discipline,
            "update_discipline": self.undo_update_discipline,
            "add_grade": self.undo_add_grade,
            "remove_grade": self.undo_remove_grade
        }
        self.__redo_dictionary = {
            "add_student": self.redo_add_student,
            "remove_student": self.redo_remove_student,
            "update_student": self.redo_update_student,
            "add_discipline": self.redo_add_discipline,
            "remove_discipline": self.redo_remove_discipline,
            "update_discipline": self.redo_update_discipline,
            "add_grade": self.redo_add_grade,
            "remove_grade": self.redo_remove_grade
        }

    def get_stack(self):
        return self.__command_stack

    def add_command_to_stack(self, job_of_the_operation, chosen_object):
        self.__the_command_from_the_top_of_the_stack += 1
        self.__command_stack.insert(self.__the_command_from_the_top_of_the_stack, [job_of_the_operation, chosen_object])
        del self.__command_stack[self.__the_command_from_the_top_of_the_stack + 1:]

    def get_last_operation(self):
        operation = self.__command_stack[self.__the_command_from_the_top_of_the_stack]
        self.__the_command_from_the_top_of_the_stack -= 1
        return operation

    def get_the_job_of_the_last_operation(self, operation):
        return operation[0]

    def get_chosen_object_of_the_last_operation(self, operation):
        return operation[1]

    def get_next_operation(self):
        operation = self.__command_stack[self.__the_command_from_the_top_of_the_stack + 1]
        self.__the_command_from_the_top_of_the_stack += 1
        return operation

    def get_last_stack_operation(self):
        return self.__command_stack[self.__the_command_from_the_top_of_the_stack]

    def call_undo(self):
        if self.__the_command_from_the_top_of_the_stack == -1:
            raise UndoException("There is nothing to undo")
        last_operation = self.get_last_operation()
        job_of_the_operation = self.get_the_job_of_the_last_operation(last_operation)
        chosen_object = self.get_chosen_object_of_the_last_operation(last_operation)
        self.__undo_dictionary[job_of_the_operation](chosen_object)

    def undo_add_student(self, student):
        self.__student_service.remove_student(student.id)

    def undo_remove_student(self, student):
        self.__student_service.add_student(student.id, student.name)
        while self.get_last_stack_operation()[0] == "remove_grade" and self.__the_command_from_the_top_of_the_stack > -1:
            self.call_undo()

    def undo_update_student(self, student):
        real_name = student.name.split(",")
        self.__student_service.update_student(student.id, real_name[0])

    def undo_add_discipline(self, discipline):
        self.__discipline_service.remove_discipline(discipline.id)

    def undo_remove_discipline(self, discipline):
        self.__discipline_service.add_discipline(discipline.id, discipline.name)
        while self.get_last_stack_operation()[0] == "remove_grade" and self.__the_command_from_the_top_of_the_stack > -1:
            self.call_undo()

    def undo_update_discipline(self, discipline):
        real_name = discipline.name.split(",")
        self.__discipline_service.update_discipline(discipline.id, real_name[0])

    def undo_add_grade(self, grade):
        self.__grade_service.remove_grade(grade.id)

    def undo_remove_grade(self, grade):
        self.__grade_service.add_grade(grade.student_id, grade.discipline_id, grade.grade_value)

    def call_redo(self):
        if self.__the_command_from_the_top_of_the_stack == len(self.__command_stack) - 1:
            raise UndoException("There is nothing to redo")
        next_operation = self.get_next_operation()
        job_of_the_operation = self.get_the_job_of_the_last_operation(next_operation)
        chosen_object = self.get_chosen_object_of_the_last_operation(next_operation)
        self.__redo_dictionary[job_of_the_operation](chosen_object)

    def redo_add_student(self, student):
        self.undo_remove_student(student)

    def redo_remove_student(self, student):
        self.undo_add_student(student)

    def redo_update_student(self, student):
        real_name = student.name.split(",")
        self.__student_service.update_student(student.id, real_name[1])

    def redo_add_discipline(self, discipline):
        self.undo_remove_discipline(discipline)

    def redo_remove_discipline(self, discipline):
        self.undo_add_discipline(discipline)

    def redo_update_discipline(self, discipline):
        real_name = discipline.name.split(",")
        self.__discipline_service.update_discipline(discipline.id, real_name[1])

    def redo_remove_grade(self, grade):
        self.__grade_service.remove_grade(self.__grade_service.search_for_grade_id_with_student_and_discipline_id(grade.student_id, grade.discipline_id))
        self.call_redo()

    def redo_add_grade(self, grade):
        self.undo_remove_grade(grade)


