class NavigationHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def to_contacts(self):
        if not self.wd.current_url.endswith("addressbook/"):
            self.wd.get("http://localhost/addressbook/")

    def to_groups(self):
        self.wd.get("http://localhost/addressbook/group.php")
