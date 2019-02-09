# -*- coding: utf-8 -*-
from utils.utils import get_random_index_from_list


def test_check_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    index = get_random_index_from_list(old_contacts)
    ln1, fn1, ad1, em1, ph1 = app.contacts.get_info_from_main_page_by_num(index)
    app.contacts.to_edit_contact_by_num(index)
    ln2, fn2, ad2, em2, ph2 = app.contacts.get_info_from_edit_page()
    assert ln1 == ln2
    assert fn2 == fn2
    assert ad1 == ad2
    assert em1 == em2
    assert ph1 == ph2
