from abc import ABC


class Note(ABC):

    def __init__(self, value, name=None, subject=None):
        self.__name = name
        self.__subject = subject
        self.__value = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


