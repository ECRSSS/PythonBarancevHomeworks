from model.groups import Group


def test_remove_group(app):
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter"))
    app.groups.to_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.delete()
