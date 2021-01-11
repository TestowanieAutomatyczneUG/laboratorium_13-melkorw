from abc import ABC, abstractmethod
from src.serv.Note import Note

class NotesStorage(ABC):
    def __init__(self, notes_storage_id):
        self.__notes_storage_id = notes_storage_id
        self.__notes_set = set()

    @property
    def notes_storage_id(self):
        return self.__notes_storage_id

    @property
    def notes_set(self):
        return self.__notes_set

    @notes_set.setter
    def notes_storage_set(self, value):
        self.__notes_set = value

    def add_note(self, note):
        number_of_notes = len(self.notes_storage_set)
        self.notes_storage_set.add(note)
        return len(self.notes_storage_set) == number_of_notes + 1

    def remove_note(self, note):
        number_of_notes = len(self.notes_storage_set)
        if not note.value == 1:
            self.notes_storage_set.remove(note)
        return len(self.notes_storage_set) == number_of_notes - 1

    def add_notes_to_one_subject(self, notes, subject_name):
        number_of_notes = len(self.notes_storage_set)
        for note in notes:
            note.subject = subject_name
            self.notes_storage_set.add(note)
        return len(self.notes_storage_set) == number_of_notes + len(notes)

    def add_notes_to_one_person(self, notes, person_name):
        number_of_notes = len(self.notes_storage_set)
        for note in notes:
            note.name = person_name
            self.notes_storage_set.add(note)
        return len(self.notes_storage_set) == number_of_notes + len(notes)

    def edit_note(self, subject_name, person_name, old_value, new_value):
        if old_value == 1:
            return False
        old_note = next((note for note in self.notes_storage_set if note.name == person_name
                         and note.subject == subject_name and note.value == old_value), None)
        if old_note is None:
            return True
        self.remove_note(old_note)
        self.add_note(Note(new_value, person_name, subject_name))
        return True
