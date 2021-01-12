from src.journal.Subject import Subject


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subjects = []
        self.warnings = []

    def get_credentials(self):
        return self.name + ' ' + self.surname

    def get_subjects(self):
        return self.subjects

    def get_warnings(self):
        return self.warnings

    def add_subject(self, subject):
        if isinstance(subject, type(Subject('Przyroda'))) is False:
            raise TypeError('Subject must be Subject type')
        for subject_a in self.subjects:
            if subject_a.get_name() == subject.get_name():
                return False
        self.subjects.append(subject)
        return True

    def remove_subject(self, name):
        for i in range(0, len(self.subjects)):
            if self.subjects[i].get_name() == name:
                del self.subjects[i]
                return True
        return False

    def get_subject_grades(self, name):
        for i in range(0, len(self.subjects)):
            if self.subjects[i].get_name() == name:
                return self.subjects[i].get_grades()
        return 0

    def average_all(self):
        suma = 0
        count = 0
        for i in range(0, len(self.subjects)):
            grades = self.subjects[i].get_grades()
            for grade in grades:
                suma += grade
                count += 1
        return suma/count

    def delete_subject_grade(self, name, el_id):
        for i in range(0, len(self.subjects)):
            if self.subjects[i].get_name() == name:
                resp = self.subjects[i].delete_grade(el_id)
                return resp
        return False

    def add_grades(self, name, grades):
        for i in range(0, len(self.subjects)):
            if self.subjects[i].get_name() == name:
                self.subjects[i].add_grades(grades)
                return True
        return False

    def edit_subject_grade(self, name, grade_id, new_value):
        for i in range(0, len(self.subjects)):
            if self.subjects[i].get_name() == name:
                response = self.subjects[i].edit_grade(grade_id, new_value)
                return response
        return False

    def add_warning(self, warning):
        if type(warning) is not str:
            raise TypeError('Warning must be string type')
        if len(warning) == 0:
            raise ValueError('Warning cannot be empty')
        self.warnings.append(warning)
        return 'Added'

    def delete_warning(self, warning_id):
        if type(warning_id) is not int:
            raise TypeError('Warning id must be int')
        if warning_id < 0 or warning_id >= len(self.warnings):
            return 'Warning with given ID does not exist'
        del self.warnings[warning_id]
        return 'Deleted'
