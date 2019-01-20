# -*- coding: utf-8 -*-
from time import sleep


class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()
        sleep(0.5)

    def login(self, user, password):
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(user)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()
