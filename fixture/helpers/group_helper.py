# -*- coding: utf-8 -*-


class GroupsHelper:
    def __init__(self,app):
        self.app = app
        self.wd = app.wd

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