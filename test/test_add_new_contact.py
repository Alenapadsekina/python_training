# -*- coding: utf-8 -*-
from model.contact import Contact

# ADD NEW CONTACT
def test_add_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
                           company="some_company", address_1="123 Tice Blvd.", mobile_phone="2013912500",
                           address_2="Woodcliff Lake", home_phone="2013912501", work_phone="2013912502", fax="2013912503",
                           email_2="test.email.2@test.com", email_3="test.email.3@test.com",
                           email_1="test.email.1@test.com", website="http://homepage.com", group_phone="8885016953", birth_day="17", birth_month="February", anniversary_date="18",
                           anniversary_month="December", anniversary_year="1990", birth_year="1990")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)



