
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create_new_contact(self, contact):
        wd = self.app.wd
        # name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(contact.company)
        # address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        # phones
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # emails and website
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(contact.website)
        # dates
        wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("aday").click()
        #Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_date)
        wd.find_element_by_name("amonth").click()
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # group
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys(contact.group_phone)
        # notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("notes notes")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
