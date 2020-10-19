Scenario Outline: Add new contact
  Given a contacts list
  Given a new contact with <first_name>, <last_name>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact


  Examples:
  | first_name | last_name |
  | FIRST_NAME_1 | LAST_NAME_1 |
  | FIRST_NAME_2 | LAST_NAME_2 |

  Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact <first_name> from the list
  Then the new contact list is equal to the old contact list with the modified contact

    Examples:
  | first_name |
  | MODIFIED FIRST NAME |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact