from model.groups import Group
from utils.utils import get_random_index_from_list


def test_remove_group(app):
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter", None))
    app.navigation.to_groups()
    old_groups = app.groups.get_groups()
    index = get_random_index_from_list(old_groups)
    app.groups.select_group_by_num_on_page(index)
    app.groups.delete()
    app.navigation.to_groups()
    new_groups = app.groups.get_groups()
    assert len(old_groups) == len(new_groups) + 1
    del old_groups[index]
    assert old_groups == new_groups

