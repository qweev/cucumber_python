Feature: lists of list story

  Scenario: scenario with list in list
    Given a system state with list in list
      """
      | firstName   | lastName | birthDate  |
      | Annie M. G. | Schmidt  | 1911-03-20 |
      | Roald       | Dahl     | 1916-09-13 |
      | Astrid      | Lindgren | 1907-11-14 |
      """
    When I do something with list in list
    Then system is in a different state with list in list
