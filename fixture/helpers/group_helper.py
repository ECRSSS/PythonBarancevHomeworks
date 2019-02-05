# -*- coding: utf-8 -*-
from model.groups import Group


class GroupsHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def type_group(self, group):
        self.app.fill_field_by_name("group_name", group.name)
        self.app.fill_field_by_name("group_header", group.header)
        self.app.fill_field_by_name("group_footer", group.footer)

    def submit(self):
        self.wd.find_element_by_name("submit").click()
        self.groups_cache = None

    def update(self):
        self.wd.find_element_by_name("update").click()
        self.groups_cache = None

    groups_cache = None

    def get_groups(self):
        if self.groups_cache is None:
            groups_elements = self.wd.find_elements_by_xpath("//span[@class='group']")
            self.groups_cache = list()
            for element in groups_elements:
                group_id = element.find_element_by_css_selector("input").get_attribute("value")
                group_name = element.text
                self.groups_cache.append(Group(group_name, None, None, group_id))
            return list(self.groups_cache)
        else:
            return list(self.groups_cache)

    def add_new_group(self, group):
        self.wd.find_element_by_name("new").click()
        self.type_group(group)
        self.submit()
        self.app.navigation.to_groups()

    def select_group_by_num_on_page(self, num):
        self.wd.find_elements_by_xpath("//span/input")[num].click()

    def delete(self):
        self.wd.find_element_by_name("delete").click()
        self.groups_cache = None

    def modify(self, group):
        self.wd.find_element_by_name("edit").click()
        self.type_group(group)
        self.update()

    def count(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def create_group_if_not_exist(self, group):
        self.app.navigation.to_groups()
        if self.count() == 0:
            self.add_new_group(group)
