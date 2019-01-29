# -*- coding: utf-8 -*-
from model.contacts import Contact

def test_add_contact(app):
    app.navigation.to_contacts()
    app.contacts.add_new_contact(Contact("first name", "middle name", "last name"))