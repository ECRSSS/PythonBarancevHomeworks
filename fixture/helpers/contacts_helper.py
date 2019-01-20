# -*- coding: utf-8 -*-


class ContactsHelper:
    def __init__(self,app):
        self.app = app
        self.wd = app.wd

    def type_contact(self, contact):
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.first_name)
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)

    def submit(self):
        self.wd.find_element_by_name("submit").click()

    def update(self):
        self.wd.find_element_by_name("update").click()

    def add_new_contact(self, contact):
        self.wd.find_element_by_xpath("//a[text()='add new']").click()
        self.type_contact(contact)
        self.submit()

    def remove_contact_by_num_on_page(self, num):
        checkbox = self.wd.find_elements_by_xpath("//td[contains(@class,'center')]/input")[num]
        checkbox.click()
        self.wd.find_element_by_xpath("//input[contains(@value,'Delete')]").click()
        self.wd.switch_to.alert.accept()

    def modify_contact_by_num_on_page(self, contact, num):
        self.wd.find_elements_by_xpath("//img[contains(@title,'Edit')]/..")[num].click()
        self.type_contact(contact)
        self.update()
