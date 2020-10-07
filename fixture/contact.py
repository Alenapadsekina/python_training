from model.contact import Contact
import re


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
            wd.find_element_by_link_text("home").click()

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
        wd.find_element_by_link_text("home").click()
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
                all_phones = elements[5].text
                all_emails = elements[4].text
                address = elements[3].text
                self.contacts_cache.append(Contact(last_name=last_name, first_name=first_name, id = id,
                                                   address_1 = address,
                                                   all_emails_from_contact_page = all_emails, all_phones_from_contact_page = all_phones))
        return self.contacts_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        rows = wd.find_elements_by_name("entry")
        for i in (len(rows)):
            contact_id = rows[i].find_elements_by_tag_name("td")[1]
            if contact_id == id:
                cell = rows.find_elements_by_tag_name("td")[7]
                cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id,
                       home_phone=homephone, work_phone=workphone, mobile_phone=mobilephone, address_1=address,
                       email_1=email1, email_2=email2, email_3=email3)

    def get_contact_from_view_page(self, index):
        self.open_contact_to_view_by_index(index)
        wd = self.app.wd
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(home_phone=homephone, work_phone=workphone,
                   mobile_phone=mobilephone)


    # SELECT CONTACT

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()



    # CRUD CONTACTS

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home").click()
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
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contacts_cache = None
