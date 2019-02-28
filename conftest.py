import pytest
import json

from fixture.application import Application
from generators.contacts_generator import get_contacts
from generators.group_generator import get_groups

fixture = None


@pytest.fixture
def app(request):
    global fixture
    path = request.config.getoption("--target")
    with open(path) as config:
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


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


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
    parser.addoption("--check_ui", action="store_true")
    parser.addoption("--url", action="store", default="http://localhost/addressbook", help="type url")
    parser.addoption("--target", action="store",
                     default="C:/Users/nngle/Documents/GitHub/PythonBarancevHomeworks/target.json", help="config file")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_groups"):
            testdata = get_groups()
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        if fixture.startswith("data_contacts"):
            testdata = get_contacts()
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
