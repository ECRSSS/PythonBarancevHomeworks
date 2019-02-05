# -*- coding: utf-8 -*-
from model.groups import Group
from utils.utils import list_sort


def test_modify_group(app):
    app.groups.create_group_if_not_exist(Group("ToModifiedName", "ToModifiedHeader", "ToModifiedFooter", None))
    app.navigation.to_groups()
    old_groups = app.groups.get_groups()
    app.groups.select_group_by_num_on_page(0)
    modified_group = Group("ModifiedName", "ModifiedHeader", "ModifiedFooter", None)
    app.groups.modify(modified_group)
    app.navigation.to_groups()
    new_groups = app.groups.get_groups()
    assert len(old_groups) == len(new_groups)
    del old_groups[0]
    old_groups.append(modified_group)
    assert list_sort(old_groups) == list_sort(new_groups)
