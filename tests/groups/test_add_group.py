# -*- coding: utf-8 -*-
from model.groups import Group

def test_add_group(app):
    app.open_addressbook_page()
    app.session.login("admin", "secret")
    app.groups.to_groups()
    app.groups.add_new_group(Group("name", "header", "footer"))
    app.session.logout()
