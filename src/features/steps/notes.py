from behave import *
from src.serv.Note import Note
from src.serv.NotesStorage import NotesStorage

use_step_matcher("re")


@given('we have notes storage')
def step_impl(context):
    context.notes_storage = NotesStorage("1")


@when('we have new note with value different than 1')
def step_impl(context):
    context.note = Note(3, "Olek", "Przyroda")


@then('we can add and remove it from storage')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_note(context.note)
    assert len(context.notes_storage.notes_set) == 1
    assert [el for el in context.notes_storage.notes_set][0].name == "Olek"
    assert context.notes_storage.remove_note(context.note)
    assert len(context.notes_storage.notes_set) == 0


@when('we have new note equal to 1')
def step_impl(context):
    context.note = Note(1, "Olek", "Przyroda")


@then('we can add but cannot remove it from storage')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_note(context.note)
    assert len(context.notes_storage.notes_set) == 1
    assert [el for el in context.notes_storage.notes_set][0].name == "Olek"
    assert not context.notes_storage.remove_note(context.note)
    assert len(context.notes_storage.notes_set) == 1


@when('we have list of notes without subject and subject name')
def step_impl(context):
    context.notes = [Note(2, "Olek"), Note(3, "Maciek")]
    context.subject_name = "Przyroda"


@then('we can add multiple notes with given subject name and remove one')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_notes_to_one_subject(context.notes, context.subject_name)
    assert len(context.notes_storage.notes_set) == 2
    assert [el for el in context.notes_storage.notes_set][0].subject == "Przyroda"
    assert context.notes_storage.remove_note(context.notes[0])
    assert len(context.notes_storage.notes_set) == 1


@when('we have list of notes without name and name of person')
def step_impl(context):
    context.notes = [Note(2, None, "Przyroda"), Note(3, None, "Niemiecki")]
    context.person_name = "Olek"


@then('we can add multiple notes with given person name and remove one')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_notes_to_one_person(context.notes, context.person_name)
    assert len(context.notes_storage.notes_set) == 2
    assert [el for el in context.notes_storage.notes_set][0].name == "Olek"
    assert context.notes_storage.remove_note(context.notes[0])
    assert len(context.notes_storage.notes_set) == 1


@when('we have subject name and person name, old value and new value')
def step_impl(context):
    context.subject_name = "Przyroda"
    context.person_name = "Olek"
    context.old_value = 2
    context.new_value = 3
    context.old_note = Note(2, "Olek", "Przyroda")


@then('we can edit one note of given old value to new value')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_note(context.old_note)
    assert len(context.notes_storage.notes_set) == 1
    assert context.notes_storage.edit_note(context.subject_name, context.person_name, context.old_value, context.new_value)
    assert [el for el in context.notes_storage.notes_set][0].value == context.new_value
    assert len(context.notes_storage.notes_set) == 1


@when('we have subject name and person name, old value equal to 1 and new value')
def step_impl(context):
    context.subject_name = "Przyroda"
    context.person_name = "Olek"
    context.old_value = 1
    context.new_value = 3
    context.old_note = Note(1, "Olek", "Przyroda")


@then('we cannot edit note of value equal to 1')
def step_impl(context):
    assert context.notes_storage.notes_storage_id == "1"
    assert context.notes_storage.add_note(context.old_note)
    assert len(context.notes_storage.notes_set) == 1
    assert not context.notes_storage.edit_note(context.subject_name, context.person_name, context.old_value, context.new_value)
    assert [el for el in context.notes_storage.notes_set][0].value == context.old_value
