def test_remove_group(app):
    app.open()
    app.session.login("admin", "secret")
    app.groups.to_groups()
    app.groups.select_group_by_num_on_page(0)
    app.groups.delete()
    app.session.logout()
