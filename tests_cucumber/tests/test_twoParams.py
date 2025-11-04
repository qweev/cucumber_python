from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/twoParamsStory.feature')

@given(parsers.cfparse("variable {x:d}"), target_fixture="state")
def given_variable(x):
    return {"value": x}

@when(parsers.cfparse("I add with {y:d}"))
def add_to_value(state, y):
    state["value"] += y

@then(parsers.cfparse("system output is {expected:d}"))
def check_output(state, expected):
    print(f"\nOutput: {state['value']}")
    assert state["value"] == expected