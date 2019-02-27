# -*- coding: utf-8 -*-
from utils.utils import get_random_index_from_list


def test_check_contact(app):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_info_from_main_page_list()
    for n in range(len(old_contacts)):
        ln1, fn1, ad1, em1, ph1 = app.contacts.get_info_from_main_page_by_num(n)
        ln2, fn2, ad2, em2, ph2 = old_contacts[n]
        fs = "%s %s %s %s %s" % (ln1, fn1, ad1, em1, ph1)
        ss = "%s %s %s %s %s" % (ln2, fn2, ad2, em2, ph2)
        assert fs == ss
