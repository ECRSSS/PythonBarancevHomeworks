# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select

from model.contacts import Contact
from utils.utils import clear


class ContactsHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def select_group(self, id):
        Select(self.wd.find_element_by_xpath("//select[@name='group']")).select_by_value(str(id))

    def add_contact_to_group_by_index_and_get_group_id(self, index):
        select = Select(self.wd.find_element_by_xpath("//select[@name='to_group']"))
        select.select_by_index(index)
        selected_value = select.first_selected_option.get_attribute('value')
        self.wd.find_element_by_xpath("//input[@name='add']").click()
        return selected_value

    def select_contact_by_num_and_get_id(self, num):
        contact = self.wd.find_element_by_xpath("//tr[" + str(num + 2) + "]//input[@name='selected[]']")
        id = contact.get_attribute("id")
        contact.click()
        return id

    def remove_from_group(self):
        self.wd.find_element_by_xpath("//input[@name='remove']")

    def type_contact(self, contact):
        self.app.fill_field_by_name("firstname", contact.first_name)
        self.app.fill_field_by_name("middlename", contact.middle_name)
        self.app.fill_field_by_name("lastname", contact.last_name)

    def submit(self):
        self.wd.find_element_by_name("submit").click()
        self.contacts_cache = None

    def update(self):
        self.wd.find_element_by_name("update").click()
        self.contacts_cache = None

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
        self.contacts_cache = None

    def modify_contact_by_num_on_page(self, contact, num):
        self.to_edit_contact_by_num(num)
        self.type_contact(contact)
        self.update()

    def to_edit_contact_by_num(self, num):
        self.wd.find_elements_by_xpath("//img[contains(@title,'Edit')]/..")[num].click()

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

    contacts_cache = None

    def get_contacts(self):
        if self.contacts_cache is None:
            contacts = self.wd.find_elements_by_xpath("//tr[@name='entry']")
            self.contacts_cache = list()
            for elm in contacts:
                elm_id = elm.find_element_by_css_selector("input").get_attribute("id")
                elm_last_name = elm.find_element_by_css_selector("td:nth-child(2)").text
                elm_first_name = elm.find_element_by_css_selector("td:nth-child(3)").text
                self.contacts_cache.append(Contact(elm_first_name, None, elm_last_name, elm_id))
            return list(self.contacts_cache)
        else:
            return list(self.contacts_cache)

    def get_info_from_main_page_by_num(self, num):
        tds = self.wd.find_elements_by_xpath("//tr[@name='entry'][%s]/td" % str(num + 1))
        last_name = tds[1].text
        first_name = tds[2].text
        address = tds[3].text
        emails = tds[4].text.replace("\n", "")
        phones = clear(tds[5].text.replace("\n", ""))
        return last_name, first_name, address, emails, phones

    def get_info_from_main_page_list(self):
        trs = self.wd.find_elements_by_xpath("//tr[@name='entry']")
        entities = list()
        for n in range(len(trs)):
            entities.append(list(self.get_info_from_main_page_by_num(n)))
        return entities

    def get_info_from_edit_page(self):
        fields = self.wd.find_elements_by_xpath("//input")

        def getval(elm):
            return elm.get_attribute("value")

        last_name = getval(fields[5])
        first_name = getval(fields[3])
        address = self.wd.find_element_by_xpath("//textarea[1]").text
        emails = getval(fields[15]) + getval(fields[16]) + getval(fields[17])
        phones = clear(getval(fields[11]) + getval(fields[12]) + getval(fields[13]) + getval(fields[21]))
        return last_name, first_name, address, emails, phones
