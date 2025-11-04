import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import re

scenarios('../features/listStory.feature')

@given('a system state with list:', target_fixture="state")
def system_state_with_list(docstring):
    return [item.strip() for item in docstring.strip().split('\n') if item.strip()]

@when("I do something with list")
def do_something_with_list(state):
    state.reverse()

@then("system is in a different state with list")
def system_in_different_state_with_list(state):
    assert state == ['wolf', 'cat', 'dog']
