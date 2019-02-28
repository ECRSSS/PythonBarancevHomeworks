# -*- coding: utf-8 -*-
from fixture.helpers.db_helper import DBHelper
from model.contacts import Contact
from model.groups import Group


def test_add_contact_to_group(app):
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.groups.create_group_if_not_exist(Group("ToRemoveName", "ToRemoveHeader", "ToRemoveFooter", None))
    app.navigation.to_contacts()
    contact_id = app.contacts.select_contact_by_num_and_get_id(0)
    group_id = app.contacts.add_contact_to_group_by_index_and_get_group_id(0)
    list_ids = list()
    for elm in app.orm.get_contacts_in_groups_list(group_id):
        list_ids.append(elm.elm_id)
    assert int(contact_id) in list_ids
