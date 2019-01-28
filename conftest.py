import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.open()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.open()
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
