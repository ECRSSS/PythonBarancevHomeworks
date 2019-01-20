# -*- coding: utf-8 -*-


def test_remove_contact(app):
    app.open()
    app.session.login("admin", "secret")
    app.contacts.remove_contact_by_num_on_page(0)
    app.session.logout()
