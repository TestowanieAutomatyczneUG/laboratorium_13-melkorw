class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def get_grade(self, grade_id):
        if type(grade_id) is not int:
            raise TypeError('Grade id must be int')
        if 0 <= grade_id < len(self.grades):
            return self.grades[grade_id]
        return 'Grade with given ID does not exist'

    def add_grades(self, new_grades):
        if type(new_grades) is not int and isinstance(new_grades,
                                                      type([])) is not True:
            raise TypeError('New grades can be only number or array')
        if type(new_grades) is int:
            if new_grades < 1 or new_grades > 6:
                raise ValueError('Grade must be positive number')
            self.grades.append(new_grades)
        else:
            if len(new_grades) == 0:
                raise ValueError('Array cannot be empty')
            if all(type(n) is int for n in new_grades) is not True:
                raise TypeError('Grade must be number')
            if all(0 < n < 7 for n in new_grades) is not True:
                raise ValueError('Grade must be positive number')
            self.grades = self.grades + new_grades

    def delete_grade(self, el_id):
        if type(el_id) is not int:
            raise TypeError('Id must be integer')
        if 0 <= el_id <= len(self.grades) - 1:
            if self.grades[el_id] == 1:
                return False
            del self.grades[el_id]
            return True
        return False

    def edit_grade(self, el_id, new_grade):
        if type(el_id) is not int or type(new_grade) is not int:
            raise TypeError('Id must be integer')
        if new_grade < 1 or new_grade > 6:
            raise ValueError('Grades are between 1 and 6')
        if 0 <= el_id <= len(self.grades) - 1:
            if self.grades[el_id] == 1:
                return False
            self.grades[el_id] = new_grade
            return True
        return False

    def average(self):
        if len(self.grades) == 0:
            return 0
        else:
            return round(sum(self.grades) / len(self.grades), 2)
