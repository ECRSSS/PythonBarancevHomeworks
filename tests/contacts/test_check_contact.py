# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_check_contact(app):
    app.navigation.to_contacts()
    orm_contacts = app.orm.get_contacts_as_strings_list()
    main_page_contacts = app.contacts.get_info_from_main_page_as_strings_list()
    for n in range(len(orm_contacts)):
        print("ORM: " + orm_contacts[n])
        print("Main: " + main_page_contacts[n])
