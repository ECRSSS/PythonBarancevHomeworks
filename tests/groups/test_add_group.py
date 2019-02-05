# -*- coding: utf-8 -*-
from model.groups import Group
from utils.utils import list_sort


def test_add_group(app):
    app.navigation.to_groups()
    old_groups = app.groups.get_groups()
    adding_group = Group("name", "header", "footer", None)
    app.groups.add_new_group(adding_group)
    app.navigation.to_groups()
    new_groups = app.groups.get_groups()
    assert len(new_groups) == len(old_groups) + 1
    old_groups.append(adding_group)
    assert list_sort(old_groups) == list_sort(new_groups)
