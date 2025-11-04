Feature: data tables type story

# !!! pytest-bdd nie obsługuje automatycznie context.table jak czysty Behave. Musisz sam parsować dane z table.

# !!! pytest-bdd nie ma natywnego wsparcia dla takich tzw. "step data tables" (tabel w kroku),
#  więc nie dostaniesz automatycznie argumentu table czy listy, aby sprarsowac trzeba regexpy ktore idealnie wylapac kroki
#  np. given, trzba idealnie lapc i parsowac step na liste w tescie
# np:
# @given(parsers.re(r'a system state with list:\n\s+"""(?P<items>.*?)\s+"""', flags=re.DOTALL), target_fixture="state")
# def system_state_with_list(items):



#Scenario: scenario with list
#  Given a system state with list:
#    """
#    dog
#    cat
#    wolf
#    """
#  When I do something with list
#  Then system is in a different state with list


#  Scenario:  scenario with list in list
#    Given a system state with list in list
#    """
#      | firstName   | lastName | birthDate  |
#      | Annie M. G. | Schmidt  | 1911-03-20 |
#      | Roald       | Dahl     | 1916-09-13 |
#      | Astrid      | Lindgren | 1907-11-14 |
#    """
#    When I do something with list in list
#    Then system is in a different state with list in list

#  Scenario:  scenario with map
#    Given a system state with map
#      |cat|catty|
#      |wolf|wolfy|
#      |dog |doggy|
#    When I do something with map
#    Then system is in a different state with map
#
#
#  Scenario:  scenario with list with map
#    Given a system state with list map
#      |name|surname|comment|anythig|
#      |cat|catty|qwwere |tyutyut   |
#      |wolf|wolfy|sdfgdgf|tyutyutyu|
#      |dog|doggy|sdfsdf  |tyutyut  |
#    When I do something with list map
#    Then system is in a different state with list map



  Scenario: Successful login for multiple users
    Given the following users exist
      | username | password |
      | alice    | pass123  |
      | bob      | secret   |
    When they try to login
    Then all users should login successfully