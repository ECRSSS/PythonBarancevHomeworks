# -*- coding: utf-8 -*-
from model.contacts import Contact


class ContactsHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def type_contact(self, contact):
        self.app.fill_field_by_name("firstname", contact.first_name)
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

    def get_contact_by_num(self, num):
        contact = self.wd.find_element_by_xpath("//tr[@name='entry'][" + str(num) + "]")
        elm_id = contact.find_element_by_css_selector("input").get_attribute("id")
        elm_last_name = contact.find_element_by_css_selector("td:nth-child(2)").text
        elm_first_name = contact.find_element_by_css_selector("td:nth-child(3)").text
        return Contact(elm_first_name, None, elm_last_name, elm_id)

    def get_contacts(self):
        contacts = self.wd.find_elements_by_xpath("//tr[@name='entry']")
        elms_list = list()
        for elm in contacts:
            elm_id = elm.find_element_by_css_selector("input").get_attribute("id")
            elm_last_name = elm.find_element_by_css_selector("td:nth-child(2)").text
            elm_first_name = elm.find_element_by_css_selector("td:nth-child(3)").text
            elms_list.append(Contact(elm_first_name, "", elm_last_name, elm_id))
        return elms_list
