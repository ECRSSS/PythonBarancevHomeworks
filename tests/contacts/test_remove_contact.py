# -*- coding: utf-8 -*-


def test_remove_contact(app):
    app.contacts.remove_contact_by_num_on_page(0)
