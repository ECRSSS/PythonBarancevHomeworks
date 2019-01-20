# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_modify_contact(app):
    app.open()
    app.session.login("admin", "secret")
    app.contacts.modify_contact_by_num_on_page(Contact("ModifiedFirstName", "ModifiedMiddleName", "ModifiedLastName"), 0)
    app.session.logout()
