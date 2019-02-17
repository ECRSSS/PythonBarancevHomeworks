# -*- coding: utf-8 -*-
from model.contacts import Contact
from utils.utils import list_sort, random_string
import pytest

testdata = [
    Contact(random_string("first", 20), random_string("middle", 20), random_string("last", 20), None)
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.navigation.to_contacts()
    old_contacts = app.contacts.get_contacts()
    app.contacts.add_new_contact(contact)
    app.navigation.to_contacts()
    new_contacts = app.contacts.get_contacts()
    assert len(new_contacts) == (len(old_contacts) + 1)
    old_contacts.append(contact)
    assert list_sort(new_contacts) == list_sort(old_contacts)
