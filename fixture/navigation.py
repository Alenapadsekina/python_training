
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8443/addressbook/group.php")


    def open_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8443/addressbook/edit.php")

