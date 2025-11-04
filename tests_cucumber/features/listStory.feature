Feature: list type story

Scenario: scenario with list
  Given a system state with list:
    """
    dog
    cat
    wolf
    """
  When I do something with list
  Then system is in a different state with list