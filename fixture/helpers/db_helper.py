# -*- coding: utf-8 -*-
from pony.orm import *

from model.contacts import Contact
from model.groups import Group
import datetime


class DBHelper:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        deprecated = Optional(datetime.datetime, column='deprecated')

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        middle_name = Optional(str, column='middlename')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(datetime.datetime, column='deprecated')

    def __init__(self, host, user, password):
        self.db.bind(provider='mysql', database='addressbook', host=host, user=user, password=password)
        self.db.generate_mapping()

    @db_session
    def get_groups_list(self):
        groups = list()
        entity_groups = list(select(g for g in DBHelper.ORMGroup if g.deprecated.date().year == 0))
        for group in entity_groups:
            groups.append(Group(group.name, group.header, group.footer, group.id))
        return groups

    @db_session
    def get_contacts_list(self):
        contacts = list()
        entity_contacts = list(select(g for g in DBHelper.ORMContact if g.deprecated.date().year == 0))
        for contact in entity_contacts:
            contacts.append(Contact(contact.first_name, contact.middle_name, contact.last_name, contact.id))
        return contacts
