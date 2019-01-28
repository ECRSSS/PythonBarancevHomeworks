def test_remove_group(app):
    app.groups.to_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.delete()
