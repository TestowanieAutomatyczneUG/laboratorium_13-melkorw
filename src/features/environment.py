from behave import *
from src.journal.Journal import Journal


def before_scenario(context, scenario):
    context.journal = Journal("1")


def after_scenario(context, scenario):
    context.journal = None
