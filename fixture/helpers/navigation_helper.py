class NavigationHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def to_contacts(self):
        if not self.wd.current_url.endswith("addressbook/") \
                and self.wd.find_elements_by_xpath("//input[@value='Send e-Mail']") == 0:
            self.wd.find_element_by_xpath("//a[text()='home']").click()

    def to_groups(self):
        if not self.wd.current_url.endswith("/group.php") \
                and self.wd.find_elements_by_xpath("//input[@value='New group']") == 0:
            self.wd.find_element_by_xpath("//a[text()='groups']").click()
