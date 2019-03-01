# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_check_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.orm.get_contacts_list()
    for n in range(len(old_contacts)):
        app.contacts.to_edit_contact_by_num(n)
        ln1, fn1, ad1, em1, ph1 = app.contacts.get_info_from_edit_page()
        contact = Contact(fn1, None, ln1, None)
        app.navigation.to_contacts()
        assert contact in old_contacts
