# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_check_contact(app):
    app.navigation.to_contacts()
    orm_contacts = app.orm.get_contacts_as_strings_list()
    main_page_contacts = app.contacts.get_info_from_main_page_as_strings_list()
    orm_contacts.sort()
    main_page_contacts.sort()
    assert orm_contacts == main_page_contacts
