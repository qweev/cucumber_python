Feature: data tables type story

# !!! pytest-bdd nie obsługuje automatycznie context.table jak czysty Behave. Musisz sam parsować dane z table.

# !!! pytest-bdd nie ma natywnego wsparcia dla takich tzw. "step data tables" (tabel w kroku),
#  więc nie dostaniesz automatycznie argumentu table czy listy, aby sprarsowac trzeba regexpy ktore idealnie wylapac kroki
#  np. given, trzba idealnie lapc i parsowac step na liste w tescie
# np:
# @given(parsers.re(r'a system state with list:\n\s+"""(?P<items>.*?)\s+"""', flags=re.DOTALL), target_fixture="state")
# def system_state_with_list(items):

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
      | bob      | mysecret |
      | john     | tajne    |
    When they try to login
    Then all users should login successfully