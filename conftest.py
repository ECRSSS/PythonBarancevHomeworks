import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    url = request.config.getoption("--url")
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser)
        fixture.open(url)
    else:
        if not fixture.is_valid():
            browser = request.config.getoption("--browser")
            fixture = Application(browser)
            fixture.open(url)
    fixture.session.ensure_login("admin", "secret")
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


