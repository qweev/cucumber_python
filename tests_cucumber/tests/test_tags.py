from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features/sixTagStory.feature')

# ==== STORY 1 ====
@given("given tag story 1", target_fixture="context")
def given_story1():
    return {"msg": "story1"}

@when("when tag story 1")
def when_story1(context):
    context["msg"] += "_processed"

@then("then tag story 1")
def then_story1(context):
    assert context["msg"] == "story1_processed"


# ==== STORY 2 ====
@given("given tag story 2", target_fixture="context")
def given_story2():
    return {"msg": "story2"}

@when("when tag story 2")
def when_story2(context):
    context["msg"] += "_processed"

@then("then tag story 2")
def then_story2(context):
    assert context["msg"] == "story2_processed"


# ==== STORY 3 ====
@given("given tag story 3", target_fixture="context")
def given_story3():
    return {"msg": "story3"}

@when("when tag story 3")
def when_story3(context):
    context["msg"] += "_processed"

@then("then tag story 3")
def then_story3(context):
    assert context["msg"] == "story3_processed"