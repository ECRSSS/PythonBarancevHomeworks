# -*- coding: utf-8 -*-
import pytest

from model.groups import Group
from utils.utils import list_sort, random_string

testdata = [
    Group(random_string("name", 20), random_string("header", 20), random_string("footer", 20), None)
    for i in range(2)
]


@pytest.mark.parametrize("adding_group", testdata)
def test_add_group(app, adding_group):
    app.navigation.to_groups()
    old_groups = app.groups.get_groups()
    app.groups.add_new_group(adding_group)
    app.navigation.to_groups()
    new_groups = app.groups.get_groups()
    assert len(new_groups) == len(old_groups) + 1
    old_groups.append(adding_group)
    assert list_sort(old_groups) == list_sort(new_groups)
