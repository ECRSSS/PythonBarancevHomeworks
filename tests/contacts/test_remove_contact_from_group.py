# -*- coding: utf-8 -*-
from fixture.helpers.db_helper import DBHelper
from model.contacts import Contact
from model.groups import Group


def test_remove_contact_from_group(app):
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter", None))
    app.navigation.to_contacts()
    group_id = app.orm.get_groups_list()[0].elm_id
    if len(app.orm.get_contacts_in_groups_list(group_id)) == 0:
        app.contacts.select_contact_by_num_and_get_id(0)
        app.contacts.add_contact_to_group_by_index_and_get_group_id(0)
    app.contacts.select_group(group_id)
    contact_id = app.contacts.select_contact_by_num_and_get_id(0)
    app.contacts.remove_from_group()
    list_ids = list()
    for elm in app.orm.get_contacts_in_groups_list(group_id):
        list_ids.append(elm.elm_id)
    assert contact_id not in list_ids
