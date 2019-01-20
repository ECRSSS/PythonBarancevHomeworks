# -*- coding: utf-8 -*-
from model.groups import Group

def test_modify_group(app):
    app.open()
    app.session.login("admin", "secret")
    app.groups.to_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.modify()
    app.groups.type_group(Group("ModifiedName", "ModifiedHeader", "ModifiedFooter"))
    app.groups.update()
    app.groups.to_groups()
    app.session.logout()
