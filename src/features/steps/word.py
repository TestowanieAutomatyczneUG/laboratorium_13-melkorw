from behave import *
import string

use_step_matcher("re")


def words_checking(words):
    if len(words) < 2:
        return Exception
    if words[0] == '' or words[1] == '':
        return ValueError
    word1, word2 = words
    x = 0
    words_a = []
    words_b = []
    while x <= 27:
        words_a.append(0)
        words_b.append(0)
        x += 1
    for letter in word1:
        if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return TypeError
        words_a[ord(letter) - ord('a')] += 1

    for letter in word2:
        if letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return TypeError
        words_b[ord(letter) - ord('a')] += 1
    y = 0
    while y < 27:
        if words_a[y] != words_b[y]:
            return False
        y += 1
    return True


@given("we have two words")
def step_impl(context):
    context.words = context.text.split(",")


@when("this words are the same")
def step_impl(context):
    context.value_of_words = context.words[0] == context.words[1]


@then("count of characters in the same words is equal and return True")
def step_impl(context):
    assert context.value_of_words is True


@when("we compare their characters")
def step_impl(context):
    context.value_of_words = words_checking(context.words)


@then("returns True")
def step_impl(context):
    assert context.value_of_words is True


@then("returns False")
def step_impl(context):
    assert context.value_of_words is False


@when("this words have equal chars but with different size")
def step_impl(context):
    word1 = context.words[0].lower()
    word2 = context.words[1].lower()
    context.value_of_words = words_checking([word1, word2])


@then("comparing them returns True")
def step_impl(context):
    assert context.value_of_words is True


@when("one is string and second not string")
def step_impl(context):
    context.value_of_words = words_checking(context.words)


@then("TypeError happens")
def step_impl(context):
    assert context.value_of_words is TypeError


@when("One word is filled and one is empty")
def step_impl(context):
    print(context.words)
    context.value_of_words = words_checking(context.words)


@then("returns ValueError")
def step_impl(context):
    assert context.value_of_words is ValueError


@given("we have one word")
def step_impl(context):
    context.words = context.text.split(",")
    if len(context.words) == 1:
        context.value = Exception
    else:
        context.value = True


@given("we have zero words")
def step_impl(context):
    context.value = Exception


@then("Exception happens")
def step_impl(context):
    assert context.value is Exception
