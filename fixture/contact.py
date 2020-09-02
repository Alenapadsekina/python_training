


class ContactHelper:

    def __init__(self, app):
        self.app = app

    # NAVIGATION
    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home page").click()

    # FILL CONTACT DATA

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # name
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        # company
        self.change_field_value("company", contact.company)
        # address
        self.change_field_value("address", contact.address_1)
        self.change_field_value("address2", contact.address_2)
        # phones
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        # emails and website
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.website)
        # dates
        #wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        #wd.find_element_by_name("bday").click()
        #wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        self.change_field_value("byear", contact.birth_year)
        #wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_date)
        #wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)

    # COUNT CONTACTS
    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    # SELECT CONTACT

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()




    # CRUD CONTACTS

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_name("update").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
