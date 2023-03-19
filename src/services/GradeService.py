from src.domain.Grade import Grade
from src.repository.GradeRepository import GradeRepository


class GradeService:
    def __init__(self):
        self.__grade_repository = GradeRepository()
        self.__grade_id = 1

    def __len__(self):
        return self.__grade_repository.__len__()

    def add_grade(self, student_id, discipline_id, grade):
        new_grade = Grade(self.__grade_id, student_id, discipline_id, grade)
        self.__grade_repository.add_grade(new_grade)
        self.__grade_id += 1

    def remove_grade(self, grade_id):
        self.__grade_repository.remove_grade_by_id(grade_id)

    def update_grade(self, grade_id, grade):
        self.__grade_repository.update_grade(grade_id, grade)

    def search_for_grade_id_with_student_and_discipline_id(self, student_id, discipline_id):
        for grade in self.get_all():
            if grade.student_id == student_id and grade.discipline_id == discipline_id:
                return grade.id

    def all_students_failing_at_one_or_more_disciplines(self, list_of_students, list_of_disciplines):
        list_of_failing_students = list()
        for student in list_of_students.get_all():
            for discipline in list_of_disciplines.get_all():
                number_of_grades = 0
                sum_of_grades = 0
                for grade in self.__grade_repository.get_all():
                    if student.id == grade.student_id and discipline.id == grade.discipline_id:
                        number_of_grades += 1
                        sum_of_grades += int(grade.grade_value)
                if float(sum_of_grades/number_of_grades) < 5:
                    list_of_failing_students.append([student, discipline, float(sum_of_grades/number_of_grades)])
        return list_of_failing_students

    def students_with_the_best_situation_in_descending_order(self, list_of_students, list_of_disciplines):
        list_of_top_students = list()
        for student in list_of_students.get_all():
            sum_of_averages = 0
            for discipline in list_of_disciplines.get_all():
                number_of_grades = 0
                sum_of_grades = 0
                for grade in self.__grade_repository.get_all():
                    if student.id == grade.student_id and discipline.id == grade.discipline_id:
                        number_of_grades += 1
                        sum_of_grades += int(grade.grade_value)
                sum_of_averages = sum_of_averages + float(sum_of_grades/number_of_grades)
            general_average = float(sum_of_averages/len(list_of_disciplines))
            list_of_top_students.append([student, general_average])
        return list(sorted(list_of_top_students, key=lambda item: item[1], reverse=True))

    def all_disciplines_sorted_by_average_grades_received_by_students(self, list_of_students, list_of_disciplines):
        list_of_sorted_disciplines = list()
        for discipline in list_of_disciplines.get_all():
            sum_of_averages = 0
            for student in list_of_students.get_all():
                number_of_grades = 0
                sum_of_grades = 0
                for grade in self.__grade_repository.get_all():
                    if student.id == grade.student_id and discipline.id == grade.discipline_id:
                        number_of_grades += 1
                        sum_of_grades += int(grade.grade_value)
                if number_of_grades > 0:
                    sum_of_averages += float(sum_of_grades/number_of_grades)
            discipline_average = float(sum_of_averages/len(list_of_students))
            if discipline_average > 0:
                list_of_sorted_disciplines.append([discipline, discipline_average])
        return list(sorted(list_of_sorted_disciplines, key=lambda item: item[1], reverse=True))

    def get_grade(self, grade_id):
        return self.__grade_repository.get_grade(grade_id)

    def get_id(self):
        return self.__grade_id - 1

    def get_all(self):
        return self.__grade_repository.get_all()
