# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

from contacts import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_addressbook_page(wd)
        self.login(wd,"admin","secret")
        self.to_contacts(wd)
        self.add_new_contact(wd,Contact("first name","middle name","last name"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self, wd, contact):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//a[text()='home page']").click()

    def to_contacts(self, wd):
        wd.find_element_by_xpath("//a[text()='add new']").click()

    def open_addressbook_page(self, wd):
        wd.get("http://localhost/addressbook")

    def login(self, wd, user, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
