# -*- coding: utf-8 -*-
import pytest

from application import Application
from groups import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_addressbook_page()
    app.login("admin", "secret")
    app.to_groups()
    app.add_new_group(Group("name", "header", "footer"))
    app.logout()
