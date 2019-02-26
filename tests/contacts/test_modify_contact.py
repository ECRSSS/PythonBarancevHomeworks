# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import list_sort, get_random_index_from_list


def test_modify_contact(app,check_ui):
    app.navigation.to_contacts()
    app.contacts.create_contact_if_not_exist(Contact("TestFirstName", "TestMiddleName", "TestLastName", None))
    app.navigation.to_contacts()
    if check_ui:
        old_contacts = app.contacts.get_contacts()
    else:
        old_contacts = app.orm.get_contacts_list()
    index = get_random_index_from_list(old_contacts)
    modified_contact = Contact("ModifiedFirstName", "ModifiedMiddleName", "ModifiedLastName", None)
    app.contacts.modify_contact_by_num_on_page(modified_contact, index)
    app.navigation.to_contacts()
    if check_ui:
        new_contacts = app.contacts.get_contacts()
    else:
        new_contacts = app.orm.get_contacts_list()
    del old_contacts[index]
    old_contacts.append(modified_contact)
    assert len(old_contacts) == len(new_contacts)
    assert list_sort(new_contacts) == list_sort(old_contacts)
