# -*- coding: utf-8 -*-
from model.contacts import Contact

def test_add_contact(app):
    app.open()
    app.session.login("admin", "secret")
    app.contacts.add_new_contact(Contact("first name", "middle name", "last name"))
    app.session.logout()
