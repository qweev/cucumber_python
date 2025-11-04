Feature: map type story

Scenario: map story
  Given a system state with map
  """
  | cat  | catty |
  | wolf | wolfy |
  | dog  | doggy |
  """
  When I do something with map
  Then system is in a different state with map