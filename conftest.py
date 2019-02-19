import pytest
import json

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    with open(request.config.getoption("--target")) as config:
        target = json.load(config)
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser)
        fixture.open(target["url"])
    else:
        if not fixture.is_valid():
            browser = request.config.getoption("--browser")
            fixture = Application(browser)
            fixture.open(target["url"])
    fixture.session.ensure_login(target["username"], target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture

    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="select browser")
    parser.addoption("--url", action="store", default="http://localhost/addressbook", help="type url")
    parser.addoption("--target", action="store", default="target.json", help="config file")
