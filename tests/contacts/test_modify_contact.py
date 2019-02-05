# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import list_sort


def test_modify_contact(app):
    app.navigation.to_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    modified_contact = Contact("ModifiedFirstName", "ModifiedMiddleName", "ModifiedLastName", None)
    app.contacts.modify_contact_by_num_on_page(modified_contact, 0)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    del old_contacts[0]
    old_contacts.append(modified_contact)
    assert len(old_contacts) == len(new_contacts)
    assert list_sort(new_contacts) == list_sort(old_contacts)
