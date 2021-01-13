Feature: Checking if both words contain the same characters
  for example abba and baab will return True (2 'a' and 2 'b')
  but abc and ab will return False (ab is missing 'c')
  also ABC equals abc (we don't think about size of letters)

  @words
  Scenario: Having both same words
    Given we have two words
    """
    kajak,kajak
    """
    When this words are the same
    Then count of characters in the same words is equal and return True

  @words
  Scenario: Having two words with equal chars
    Given we have two words
    """
    abba,baab
    """
    When we compare their characters
    Then returns True

  @words
  Scenario: Having two words with different chars
    Given we have two words
    """
    abc,abd
    """
    When we compare their characters
    Then returns False

  @words
  Scenario: Having one word in small letter and one in capital
    Given we have two words
    """
    word,WORD
    """
    When this words have equal chars but with different size
    Then comparing them returns True

  @words
  Scenario: Having one word and one number
    Given we have two words
    """
    word,1
    """
    When one is string and second not string
    Then TypeError happens

  @words
  Scenario: Having one word and one empty word
    Given we have two words
    """
    word,
    """
    When One word is filled and one is empty
    Then returns ValueError

  @words
  Scenario: Having only one word
    Given we have one word
    """
    word
    """
    Then Exception happens

  @words
  Scenario: Having zero words
    Given we have zero words
    Then Exception happens




