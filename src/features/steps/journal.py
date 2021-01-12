from behave import *
from src.journal.Student import Student
from src.journal.Subject import Subject

use_step_matcher("re")


@given('we have Student in Journal')
def step_impl(context):
    context.journal.add_student('Olek', 'Wardyn')


@when('we have new Subject')
def step_impl(context):
    context.subject = Subject("Przyroda")


@then('we can add and remove it from student')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject('Olek', 'Wardyn', context.subject)
    assert len(context.journal.get_student_subjects('Olek', 'Wardyn')) == 1
    assert context.journal.remove_student_subject('Olek', 'Wardyn', 'Przyroda')
    assert len(context.journal.get_student_subjects('Olek', 'Wardyn')) == 0


@then('we cannot add it to student twice')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject('Olek', 'Wardyn', context.subject)
    assert len(context.journal.get_student_subjects('Olek', 'Wardyn')) == 1
    assert not context.journal.add_student_subject('Olek', 'Wardyn', context.subject)
    assert len(context.journal.get_student_subjects('Olek', 'Wardyn')) == 1


@when('we have new warning')
def step_impl(context):
    context.warning = 'warning'


@then('we can add and remove this warning from student')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_warning('Olek', 'Wardyn', context.warning)
    assert len(context.journal.get_student_warnings('Olek', 'Wardyn')) == 1
    assert context.journal.delete_student_warning('Olek', 'Wardyn', 0)
    assert len(context.journal.get_student_warnings('Olek', 'Wardyn')) == 0


@given('we have Student and his Subject in Journal')
def step_impl(context):
    context.journal.add_student('Olek', 'Wardyn')
    context.journal.add_student_subject('Olek', 'Wardyn', Subject('Przyroda'))


@when('we have new grade')
def step_impl(context):
    context.grade = 3


@then('we can add and remove this grade from student\'s subject')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.grade)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 1
    assert context.journal.delete_student_subject_grade('Olek', 'Wardyn', 'Przyroda', 0)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 0


@when('we have new grade equal to 1')
def step_impl(context):
    context.grade = 1


@then('we can add but cannot remove this grade from student\'s subject')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.grade)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 1
    assert not context.journal.delete_student_subject_grade('Olek', 'Wardyn', 'Przyroda', 0)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 1


@when('we have two grades')
def step_impl(context):
    context.grades = [2, 4]


@then('we can get average of grades of this Subject')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.grades)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 2
    assert context.journal.get_student_subject_average('Olek', 'Wardyn', 'Przyroda') == 3

@when('we have old grade different than 1 and new grade')
def step_impl(context):
    context.old_grade = 2
    context.new_grade = 4

@then('we can edit old grade to a new grade')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.old_grade)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 1
    assert context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')[0] == 2
    assert context.journal.edit_student_subject_grade('Olek', 'Wardyn', 'Przyroda', 0, context.new_grade)
    assert context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')[0] == 4

@when('we have old grade equal to 1 and new grade')
def step_impl(context):
    context.old_grade = 1
    context.new_grade = 4

@then('we cannot edit old grade to a new grade')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.old_grade)
    assert len(context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')) == 1
    assert context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')[0] == 1
    assert not context.journal.edit_student_subject_grade('Olek', 'Wardyn', 'Przyroda', 0, context.new_grade)
    assert context.journal.get_student_subject_grades('Olek', 'Wardyn', 'Przyroda')[0] == 1

@given('we have Student and two of his Subjects in Journal')
def step_impl(context):
    context.journal.add_student('Olek', 'Wardyn')
    context.journal.add_student_subject('Olek', 'Wardyn', Subject('Przyroda'))
    context.journal.add_student_subject('Olek', 'Wardyn', Subject('Polski'))


@when('we have two grades in one and two grades in second subject')
def step_impl(context):
    context.grades1 = [2, 4]
    context.grades2 = [4, 6]


@then('we can get average of all student grades')
def step_impl(context):
    assert context.journal.journal_id == "1"
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Przyroda', context.grades1)
    assert context.journal.add_student_subject_grades('Olek', 'Wardyn', 'Polski', context.grades2)
    assert context.journal.get_student_average('Olek', 'Wardyn') == 4
