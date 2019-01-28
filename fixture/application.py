# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.helpers.contacts_helper import ContactsHelper
from fixture.helpers.group_helper import GroupsHelper
from fixture.helpers.session_helper import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.groups = GroupsHelper(self)
        self.contacts = ContactsHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open(self):
        self.wd.get("http://localhost/addressbook")

    def destroy(self):
        self.wd.quit()

    def fill_field_by_name(self, name, text):
        if text is not None:
            e = self.wd.find_element_by_name(name)
            e.clear()
            e.send_keys(text)
