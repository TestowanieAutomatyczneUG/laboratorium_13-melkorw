from src.journal.Student import Student


def student_checking(first_name, second_name, students):
    if type(first_name) is not str or type(second_name) is not str:
        raise TypeError('Values must be string type')
    if len(first_name) == 0 or len(second_name) == 0:
        raise ValueError('Values must be not empty strings')
    name = first_name + ' ' + second_name
    for student in students:
        if student.get_credentials() == name:
            return student
    return 'Student does not exist'


class Journal:
    def __init__(self, journal_id):
        self.journal_id = journal_id
        self.students = []

    def add_student(self, first_name, second_name):
        if type(first_name) is not str or type(second_name) is not str:
            raise TypeError('Values must be string type')
        if len(first_name) == 0 or len(second_name) == 0:
            raise ValueError('Values must be not empty strings')
        student = Student(first_name, second_name)
        for student_i in self.students:
            if student.get_credentials() == student_i.get_credentials():
                return False
        self.students.append(student)
        return True

    def add_student_subject(self, first_name, second_name, subject):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return False
        response = check.add_subject(subject)
        return response

    def get_student_subjects(self, first_name, second_name):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.get_subjects()
        return response

    def add_student_subject_grades(self, first_name, second_name, subject,
                                   grades):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.add_grades(subject, grades)
        return response

    def get_student_subject_grades(self, first_name, second_name, subject):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.get_subject_grades(subject)
        return response

    def remove_student_subject(self, first_name, second_name, subject):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return False
        response = check.remove_subject(subject)
        return response

    def edit_student_subject_grade(self, first_name, second_name, subject,
                                   grade_id, new_grade):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.edit_subject_grade(subject, grade_id, new_grade)
        return response

    def delete_student_subject_grade(self, first_name, second_name, subject,
                                     grade_id):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.delete_subject_grade(subject, grade_id)
        return response

    def get_student_subject_average(self, first_name, second_name, subject):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.get_subject_grades(subject)
        sum = 0
        for el in response:
            sum += el
        count = len(response)
        return sum / count

    def get_student_average(self, first_name, second_name):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.average_all()
        return response

    def add_student_warning(self, first_name, second_name, warning):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.add_warning(warning)
        return response

    def get_student_warnings(self, first_name, second_name):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return False
        response = check.get_warnings()
        return response

    def delete_student_warning(self, first_name, second_name, warning_id):
        check = student_checking(first_name, second_name, self.students)
        if check == 'Student does not exist':
            return check
        response = check.delete_warning(warning_id)
        return response
