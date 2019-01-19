# -*- coding: utf-8 -*-
from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def add_new_group(self, group):
        self.wd.find_element_by_name("new").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.wd.find_element_by_name("submit").click()
        self.wd.find_element_by_link_text("group page").click()

    def to_groups(self):
        self.wd.find_element_by_xpath("//a[text()='groups']").click()

    def open_addressbook_page(self):
        self.wd.get("http://localhost/addressbook")

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

    def login(self, user, password):
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(user)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def destroy(self):
        self.wd.quit()
