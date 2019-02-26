# -*- coding: utf-8 -*-
from utils.utils import list_sort


def test_add_contact(app, data_contacts,check_ui):
    contact = data_contacts
    app.navigation.to_contacts()
    if check_ui:
        old_contacts = app.contacts.get_contacts()
    else:
        old_contacts = app.orm.get_contacts_list()
    len_old=len(old_contacts)
    app.contacts.add_new_contact(contact)
    app.navigation.to_contacts()
    if check_ui:
        new_contacts = app.contacts.get_contacts()
    else:
        new_contacts = app.orm.get_contacts_list()
    assert len(new_contacts) == (len_old + 1)
    old_contacts.append(contact)
    assert list_sort(new_contacts) == list_sort(old_contacts)
