from model.groups import Group


def test_remove_group(app):
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter", None))
    app.navigation.to_groups()
    old_groups = app.groups.get_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.delete()
    app.navigation.to_groups()
    new_groups = app.groups.get_groups()
    assert len(old_groups) == len(new_groups) + 1
    del old_groups[0]
    assert old_groups == new_groups

