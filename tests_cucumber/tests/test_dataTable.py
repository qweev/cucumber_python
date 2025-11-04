import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/fourDataTableTypesStory.feature')

# Fikcyjna baza danych
VALID_USERS = {
    "alice": "pass123",
    "bob": "secret",
    "charlie": "hunter2"
}

@pytest.fixture
def user_data():
    return {"users": [], "results": []}

@given(parsers.parse("the following users exist\n{table}"))
def users_exist(table, user_data):
    lines = [line.strip() for line in table.strip().split('\n')]
    headers = lines[0].split('|')[1:-1]
    for line in lines[1:]:
        cols = [col.strip() for col in line.split('|')[1:-1]]
        user_data["users"].append(dict(zip(headers, cols)))

@when("they try to login")
def they_login(user_data):
    for user in user_data["users"]:
        username = user["username"]
        password = user["password"]
        success = VALID_USERS.get(username) == password
        user_data["results"].append(success)

@then("all users should login successfully")
def check_login_results(user_data):
    assert all(user_data["results"]), "One or more logins failed"