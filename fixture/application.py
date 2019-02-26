# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.helpers.contacts_helper import ContactsHelper
from fixture.helpers.db_helper import DBHelper
from fixture.helpers.group_helper import GroupsHelper
from fixture.helpers.navigation_helper import NavigationHelper
from fixture.helpers.session_helper import SessionHelper


class Application:
    def __init__(self, browser):
        self.wd = self.select_browser(browser)
        self.wd.implicitly_wait(1.5)
        self.session = SessionHelper(self)
        self.groups = GroupsHelper(self)
        self.contacts = ContactsHelper(self)
        self.navigation = NavigationHelper(self)
        self.orm = DBHelper(host='127.0.0.1', user='root', password='')

    def select_browser(self, browser):
        if browser == "firefox":
            return webdriver.Firefox()
        elif browser == "ie":
            return webdriver.Ie()
        elif browser == "chrome":
            return webdriver.Chrome("C:\Windows\SysWOW64\chromedriver.exe")
        else:
            raise Exception("передан неверный параметр")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open(self, url):
        self.wd.get(url)

    def destroy(self):
        self.wd.quit()

    def fill_field_by_name(self, name, text):
        if text is not None:
            e = self.wd.find_element_by_name(name)
            e.clear()
            e.send_keys(text)
