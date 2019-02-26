from model.groups import Group
from utils.utils import get_random_index_from_list, list_sort


def test_remove_group(app, check_ui):
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter", None))
    app.navigation.to_groups()
    if check_ui:
        old_groups = app.groups.get_groups()
    else:
        old_groups = app.orm.get_groups_list()
    index = get_random_index_from_list(old_groups)
    app.groups.select_group_by_num_on_page(index)
    app.groups.delete()
    app.navigation.to_groups()
    if check_ui:
        new_groups = app.groups.get_groups()
    else:
        new_groups = app.orm.get_groups_list()
    assert len(old_groups) == len(new_groups) + 1
    del old_groups[index]
    assert list_sort(old_groups) == list_sort(new_groups)
