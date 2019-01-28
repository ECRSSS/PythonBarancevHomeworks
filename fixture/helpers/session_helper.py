# -*- coding: utf-8 -*-
from time import sleep


class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()
        sleep(0.5)

    def ensure_logout(self):
        if len(self.wd.find_elements_by_link_text("Logout")) > 0:
            self.logout()

    def login(self, user, password):
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(user)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_login_in(self):
        if len(self.wd.find_elements_by_xpath("//input[@value='Login']")) > 0:
            return False
        else:
            return True

    def is_login_in_as(self, user):
        if self.wd.find_element_by_xpath("//form/b").text == "(" + user + ")":
            return True
        else:
            return False

    def ensure_login(self, user, password):
        if self.is_login_in():
            if self.is_login_in_as(user):
                return
            else:
                self.logout()
        self.login(user, password)
