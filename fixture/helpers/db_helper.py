# -*- coding: utf-8 -*-
from pony.orm import *

from model.contacts import Contact
from model.groups import Group
import datetime


def check_none(string):
    if string is None:
        return ""
    else:
        return string


class DBHelper:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        deprecated = Optional(datetime.datetime, column='deprecated')
        contacts = Set(lambda: DBHelper.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        middle_name = Optional(str, column='middlename')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(datetime.datetime, column='deprecated')
        groups = Set(lambda: DBHelper.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts',
                     lazy=True)

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
    def get_contacts_in_groups_list(self, group_id):
        orm_group = list(select(g for g in DBHelper.ORMGroup if g.id == group_id))[0]
        contacts = list()
        for contact in orm_group.contacts:
            contacts.append(Contact(contact.first_name, contact.middle_name, contact.last_name, contact.id))
        return contacts

    @db_session
    def get_contacts_list(self):
        contacts = list()
        entity_contacts = list(select(g for g in DBHelper.ORMContact if g.deprecated.date().year == 0))
        for contact in entity_contacts:
            contacts.append(Contact(contact.first_name, contact.middle_name, contact.last_name, contact.id))
        return contacts

    @db_session
    def get_contacts_as_strings_list(self):
        contacts = list()
        entity_contacts = list(select(g for g in DBHelper.ORMContact if g.deprecated.date().year == 0))
        for contact in entity_contacts:
            contacts.append(
                check_none(contact.last_name)
                + check_none(contact.first_name)
                + check_none(contact.address)
                + check_none(contact.email) + check_none(contact.email2)
                + check_none(contact.email3)
                + check_none(contact.home)
                + check_none(contact.mobile) + check_none(contact.work))
        return contacts
