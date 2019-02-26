# -*- coding: utf-8 -*-
from utils.utils import list_sort


def test_add_group(app, data_groups, check_ui):
    adding_group = data_groups
    app.navigation.to_groups()
    if check_ui:
        old_groups = app.groups.get_groups()
    else:
        old_groups = app.orm.get_groups_list()
    app.groups.add_new_group(adding_group)
    app.navigation.to_groups()
    if check_ui:
        new_groups = app.groups.get_groups()
    else:
        new_groups = app.orm.get_groups_list()
    assert len(new_groups) == len(old_groups) + 1
    old_groups.append(adding_group)
    assert list_sort(old_groups) == list_sort(new_groups)
