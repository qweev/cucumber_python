import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('../features/lists_of_dicts.feature')

@given('a system state with list in list', target_fixture="state")
def system_state_with_list_in_list(docstring):
    # Parse the docstring table into a list of dicts
    lines = [line.strip() for line in docstring.strip().split('\n') if line.strip()]
    headers = [h.strip() for h in lines[0].split('|')[1:-1]]
    data = []
    for row in lines[1:]:
        values = [v.strip() for v in row.split('|')[1:-1]]
        data.append(dict(zip(headers, values)))
    return data

# output:
# [
#     {'firstName': 'Annie M. G.', 'lastName': 'Schmidt', 'birthDate': '1911-03-20'},
#     {'firstName': 'Roald', 'lastName': 'Dahl', 'birthDate': '1916-09-13'},
#     {'firstName': 'Astrid', 'lastName': 'Lindgren', 'birthDate': '1907-11-14'}
# ]

@when('I do something with list in list')
def do_something_with_list_in_list(state):
    # Example: reverse the list
    state.reverse()

@then('system is in a different state with list in list')
def system_is_in_different_state_with_list_in_list(state):
    # Example assertion: check the list is reversed
    assert state[0]['firstName'] == 'Astrid'
    assert state[-1]['firstName'] == 'Annie M. G.'
