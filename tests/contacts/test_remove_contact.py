# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import get_random_index_from_list, list_sort


def test_remove_contact(app,check_ui):
    app.navigation.to_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    if check_ui:
        old_contacts = app.contacts.get_contacts()
    else:
        old_contacts = app.orm.get_contacts_list()
    len_contacts = len(old_contacts)
    index = get_random_index_from_list(old_contacts)
    app.navigation.to_contacts()
    app.contacts.remove_contact_by_num_on_page(index)
    app.navigation.to_contacts()
    if check_ui:
        new_contacts = app.contacts.get_contacts()
    else:
        new_contacts = app.orm.get_contacts_list()
    assert len(new_contacts) == len_contacts - 1
    del old_contacts[index]
    assert list_sort(new_contacts) == list_sort(old_contacts)
