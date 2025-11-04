import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/mapStory.feature')

# tez dziala ale trudniejsze
# @given(parsers.parse("a system state with map:\n\"\"\"\n{table}\n\"\"\""), target_fixture="state")
# def system_state_with_map(table):
#     lines = [line.strip() for line in table.strip().split('\n') if line.strip()]
#     pairs = [line.split('|')[1:-1] for line in lines]
#     return {k.strip(): v.strip() for k, v in pairs}

@given('a system state with map', target_fixture="state")
def system_state_with_map(docstring):
    lines = [line.strip() for line in docstring.strip().split('\n') if line.strip()]
    pairs = [line.split('|')[1:-1] for line in lines]
    return {k.strip(): v.strip() for k, v in pairs}

@when("I do something with map")
def do_something_with_map(state):
    # Example: reverse keys and values
    state.clear()
    state.update({'catty': 'cat', 'wolfy': 'wolf', 'doggy': 'dog'})

@then("system is in a different state with map")
def system_in_different_state_with_map(state):
    assert state == {'catty': 'cat', 'wolfy': 'wolf', 'doggy': 'dog'}
