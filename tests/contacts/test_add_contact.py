# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import list_sort


def test_add_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    contact = Contact("first name", "middle name", "last name", None)
    app.contacts.add_new_contact(contact)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    assert len(new_contacts) == (len(old_contacts) + 1)
    old_contacts.append(contact)
    assert list_sort(new_contacts) == list_sort(old_contacts)
