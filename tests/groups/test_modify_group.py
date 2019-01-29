# -*- coding: utf-8 -*-
from model.groups import Group

def test_modify_group(app):
    app.groups.create_group_if_not_exist(Group("ToModifiedName", "ToModifiedHeader", "ToModifiedFooter"))
    app.navigation.to_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.modify(Group("ModifiedName", "ModifiedHeader", "ModifiedFooter"))