# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_remove_contact(app):
    app.contacts.to_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName"))
    app.contacts.to_contacts()
    app.contacts.remove_contact_by_num_on_page(0)
