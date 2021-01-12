Feature: Journal of class
  Journal allows to storage students with their subjects and grades

  Scenario: Adding new subject to student
    Given we have Student in Journal
    When we have new Subject
    Then we can add and remove it from student


  Scenario: Adding duplicated subject to student
    Given we have Student in Journal
    When we have new Subject
    Then we cannot add it to student twice


  Scenario: Adding new warning to student
    Given we have Student in Journal
    When we have new warning
    Then we can add and remove this warning from student


  Scenario: Adding new grade different than 1 to student's subject
    Given we have Student and his Subject in Journal
    When we have new grade
    Then we can add and remove this grade from student's subject

  Scenario: Adding new grade equal to 1 to student's subject
    Given we have Student and his Subject in Journal
    When we have new grade equal to 1
    Then we can add but cannot remove this grade from student's subject


  Scenario: Getting Average of Subject grades
    Given we have Student and his Subject in Journal
    When we have two grades
    Then we can get average of grades of this Subject

  Scenario: Editing note of subject different than 1
    Given we have Student and his Subject in Journal
    When we have old grade different than 1 and new grade
    Then we can edit old grade to a new grade

  Scenario: Editing note of subject equal to 1
    Given we have Student and his Subject in Journal
    When we have old grade equal to 1 and new grade
    Then we cannot edit old grade to a new grade

  Scenario: Getting Average of All Subjects
    Given we have Student and two of his Subjects in Journal
    When we have two grades in one and two grades in second subject
    Then we can get average of all student grades

