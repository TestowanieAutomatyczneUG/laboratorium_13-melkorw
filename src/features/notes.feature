Feature: Notes Storage Behaviour
  Notes storage allows user to manage student notes
  (In details: to add, remove and get notes)

  Scenario: Adding note different than 1
     Given we have notes storage
      When we have new note with value different than 1
      Then we can add and remove it from storage

  Scenario: Adding note equal 1
    Given we have notes storage
    When we have new note equal to 1
    Then we can add but cannot remove it from storage

  Scenario: Adding notes to one subject
    Given we have notes storage
    When we have list of notes without subject and subject name
    Then we can add multiple notes with given subject name and remove one

  Scenario: Adding notes to one person
    Given we have notes storage
    When we have list of notes without name and name of person
    Then we can add multiple notes with given person name and remove one

  Scenario: Editing note value with value different than 1
    Given we have notes storage
    When we have subject name and person name, old value and new value
    Then we can edit one note of given old value to new value

  Scenario: Editing note value with value equal to 1
    Given we have notes storage
    When we have subject name and person name, old value equal to 1 and new value
    Then we cannot edit note of value equal to 1
