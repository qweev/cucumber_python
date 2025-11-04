from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/threeTableParamsStory.feature')


@given(parsers.cfparse("three variable {aParam:d}"), target_fixture="state")
def three_variable(aParam):
    return {"value": aParam}


@when(parsers.cfparse("three I add with {bParam:d}"))
def three_add(state, bParam):
    state["value"] += bParam


@then(parsers.cfparse("three system output is {valueParam:d}"))
def three_output(state, valueParam):
    print(f"\nOutput: {state['value']}")
    assert state["value"] == valueParam