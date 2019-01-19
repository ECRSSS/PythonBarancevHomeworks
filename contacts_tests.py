# -*- coding: utf-8 -*-
import pytest

from application import Application
from contacts import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_addressbook_page()
    app.login("admin", "secret")
    app.to_contacts()
    app.add_new_contact(Contact("first name", "middle name", "last name"))
    app.logout()
