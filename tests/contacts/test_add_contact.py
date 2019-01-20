# -*- coding: utf-8 -*-
from model.contacts import Contact

def test_add_contact(app):
    app.open_addressbook_page()
    app.session.login("admin", "secret")
    app.contacts.to_contacts()
    app.contacts.add_new_contact(Contact("first name", "middle name", "last name"))
    app.session.logout()
