Scenario Outline: Add new group
  Given a group list
  Given a new group with <name>, <header>, <footer>
  When I add the group to the list
  Then the new group list is equal to the old group list with the added group


  Examples:
  | name | header | footer |
  | NAME_1 | HEADER_1 | FOOTER_1 |
  | NAME_2 | HEADER_2 | FOOTER_2 |

Scenario: Modify a group
  Given a non-empty group list
  Given a random group from the list
  When I modify the group <name> from the list
  Then the new group list is equal to the old group list with the modified group

    Examples:
  | name |
  | MODIFIED NAME |

Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old group list without the deleted group

