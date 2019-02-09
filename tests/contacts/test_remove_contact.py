# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import get_random_index_from_list


def test_remove_contact(app):
    app.navigation.to_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    old_contacts = app.contacts.get_contacts()
    index = get_random_index_from_list(old_contacts)
    app.navigation.to_contacts()
    app.contacts.remove_contact_by_num_on_page(index)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    assert len(new_contacts) == len(old_contacts) - 1
    del old_contacts[index]
    assert new_contacts == old_contacts
