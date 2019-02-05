# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_remove_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.navigation.to_contacts()
    app.contacts.get_contact_by_num(1)
    app.contacts.remove_contact_by_num_on_page(0)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    if len(new_contacts) > 0:
        assert len(new_contacts) == len(old_contacts) - 1
        del old_contacts[0]
    else:
        assert len(new_contacts) == len(old_contacts)
    assert new_contacts == old_contacts
