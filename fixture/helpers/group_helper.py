# -*- coding: utf-8 -*-


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

    def update(self):
        self.wd.find_element_by_name("update").click()

    def to_groups(self):
        self.wd.get("http://localhost/addressbook/group.php")

    def add_new_group(self, group):
        self.wd.find_element_by_name("new").click()
        self.type_group(group)
        self.submit()
        self.to_groups()

    def select_group_by_num_on_page(self, num):
        self.wd.find_elements_by_xpath("//span/input")[num].click()

    def delete(self):
        self.wd.find_element_by_name("delete").click()

    def modify(self, group):
        self.wd.find_element_by_name("edit").click()
        self.type_group(group)
        self.update()

    def count(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def create_group_if_not_exist(self, group):
        self.to_groups()
        if self.count() == 0:
            self.add_new_group(group)
