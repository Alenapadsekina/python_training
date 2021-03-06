from sys import maxsize
class Contact:
    def __init__(self, id = None, first_name = None, middle_name = None, last_name = None, nickname = None,
                 company = None, all_phones_from_contact_page = None, address_1 = None, mobile_phone = None, address_2 = None, home_phone = None,
                 work_phone = None, fax = None,
                 all_emails_from_contact_page = None, email_1 = None, email_2 = None, email_3 = None, website = None,
                 group_phone = None, birth_day = None, birth_month = None, anniversary_date = None,
                 anniversary_month = None, anniversary_year = None, birth_year = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.all_phones_from_contact_page = all_phones_from_contact_page
        self.address_1 = address_1
        self.mobile_phone = mobile_phone
        self.address_2 = address_2
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.fax = fax
        self.address_1 = address_1
        self.all_emails_from_contact_page = all_emails_from_contact_page
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.website = website
        self.group_phone = group_phone
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_date = anniversary_date
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.id = id


    def __repr__(self):
        return "%s:%s %s %s %s" % (self.id, self.last_name, self.first_name, self.all_phones_from_contact_page, self.all_emails_from_contact_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
