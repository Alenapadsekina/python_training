from model.contact import Contact


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
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    # CACHE
    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                elements = element.find_elements_by_tag_name("td")
                last_name = elements[1].text
                first_name = elements[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(Contact(last_name=last_name, first_name=first_name, id = id))
        return self.contacts_cache


    # SELECT CONTACT

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)



    # CRUD CONTACTS

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        #self.return_to_home_page()
        self.contacts_cache = None


    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_name("update").click()

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.select_contact_by_index(0)