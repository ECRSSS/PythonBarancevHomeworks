# -*- coding: utf-8 -*-
from model.groups import Group

def test_add_group(app):
    app.groups.to_groups()
    app.groups.add_new_group(Group("name", "header", "footer"))
