# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

#EXAMPLE

def random_alphanumeric(maxlen):
    symbols = string.ascii_letters + string.digits  + ' '# + string.punctuation
    return ''.join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_numeric(maxlen):
    symbols = string.digits  + ' '# + string.punctuation
    return ''.join(random.choice(symbols) for i in range(maxlen))



testdata = [
    # EMPTY CONTACT
    Contact(first_name="", middle_name="", last_name="", nickname="",
            company="", address_1="",
            mobile_phone="", home_phone="", work_phone="",
            address_2="", fax="",
            email_1="",
            email_2="",
            email_3="",
            website="", group_phone="", birth_day="", birth_month="", anniversary_date="",
            anniversary_month="", anniversary_year="", birth_year="")] + [
    # RANDOM CONTACT
    Contact(first_name="FN_"+random_alphanumeric(5), middle_name="MN_"+random_alphanumeric(5), last_name="LN_"+random_alphanumeric(5), nickname="NN_"+random_alphanumeric(5),
            company="C_"+random_alphanumeric(5), address_1="A1_"+random_numeric(4)+" "+random_alphanumeric(8),
            mobile_phone="MP_"+random_numeric(11), home_phone="HP_"+random_numeric(11), work_phone="WP_"+random_numeric(11),
            address_2="A2_"+random_numeric(4)+" "+random_alphanumeric(8), fax="F_"+random_numeric(11),
            email_1="E1_"+random_alphanumeric(8)+"@"+random_alphanumeric(8)+".com",
            email_2="E2_"+random_alphanumeric(8)+"@"+random_alphanumeric(8)+".com",
            email_3="E3_"+random_alphanumeric(8)+"@"+random_alphanumeric(8)+".com",
            website="http://homepage.com", group_phone="GP_"+random_numeric(11), birth_day="17", birth_month="February", anniversary_date="18",
            anniversary_month="December", anniversary_year="1990", birth_year="1990")
    for i in range (5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

# ADD NEW CONTACT
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)



