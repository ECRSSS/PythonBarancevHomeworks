# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ContactsHelper:
    def __init__(self,app):
        self.app = app
        self.wd = app.wd

    def type_contact(self, contact):
        self.app.fill_field_by_name("firstname",contact.first_name)
        self.app.fill_field_by_name("middlename", contact.middle_name)
        self.app.fill_field_by_name("lastname", contact.last_name)

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
        self.wd.find_element_by_xpath("//*[text()='Record successful deleted']")

    def modify_contact_by_num_on_page(self, contact, num):
        self.wd.find_elements_by_xpath("//img[contains(@title,'Edit')]/..")[num].click()
        self.type_contact(contact)
        self.update()

    def count(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def create_contact_if_not_exist(self, contact):
        if self.count() == 0:
            self.add_new_contact(contact)

    def to_contacts(self):
        self.wd.get("http://localhost/addressbook")
        self.wd.find_element_by_xpath("//a[text()='home']").click()
