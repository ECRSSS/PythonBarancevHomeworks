# -*- coding: utf-8 -*-


class ContactsHelper:
    def __init__(self,app):
        self.app = app
        self.wd = app.wd

    def add_new_contact(self, contact):
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.first_name)
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.wd.find_element_by_name("submit").click()
        self.wd.find_element_by_xpath("//a[text()='home page']").click()

    def to_contacts(self):
        self.wd.find_element_by_xpath("//a[text()='add new']").click()