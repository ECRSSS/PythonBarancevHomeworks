# -*- coding: utf-8 -*-
from utils.utils import list_sort


def test_add_contact(app, data_contacts):
    contact = data_contacts
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    app.contacts.add_new_contact(contact)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    assert len(new_contacts) == (len(old_contacts) + 1)
    old_contacts.append(contact)
    assert list_sort(new_contacts) == list_sort(old_contacts)
