# -*- coding: utf-8 -*-
from random import randrange

from model.contacts import Contact


def test_remove_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    index = None
    if len(old_contacts) == 0:
        index = 0
    else:
        index = randrange(len(old_contacts))
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.navigation.to_contacts()
    app.contacts.remove_contact_by_num_on_page(index)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    if len(new_contacts) > 0:
        assert len(new_contacts) == len(old_contacts) - 1
        del old_contacts[index]
    else:
        assert len(new_contacts) == len(old_contacts)
    assert new_contacts == old_contacts
