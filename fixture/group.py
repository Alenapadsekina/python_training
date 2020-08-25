def fill_group_form(self, group):
    wd = self.app.wd
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)

class GroupHelper:

    def __init__(self, app):
        self.app = app




    def create_new_group(self, group):
        # fill new group form
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        fill_group_form(self, group)
        # submit group
        wd.find_element_by_name("submit").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        # find 1st group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # edit group data
        fill_group_form(self, group)
        # submit group
        wd.find_element_by_name("update").click()




    def delete_first_group(self):
        wd = self.app.wd
        # find 1st group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()

