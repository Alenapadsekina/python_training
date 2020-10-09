# -*- coding: utf-8 -*-
from model.contact import Contact

# EDIT 1ST CONTACT
def test_add_new_contact(app, db, check_ui):
    if app.contact.count()==0:
        app.contact.create_new_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
                    company="some_company", address_1="123 Tice Blvd.", mobile_phone="2013912500",
                    address_2="Woodcliff Lake", home_phone="2013912501", work_phone="2013912502", fax="2013912503",
                    email_2="test.email.2@test.com", email_3="test.email.3@test.com",
                    email_1="test.email.1@test.com", website="http://homepage.com", group_phone="8885016953",
                    birth_day="17", birth_month="February", anniversary_date="18",
                    anniversary_month="December", anniversary_year="1990", birth_year="1990"))

    contact = Contact(first_name="EDITED FIRST NAME", middle_name="", last_name="EDITED LAST NAME", nickname="",
                           company="", address_1="", mobile_phone="", address_2="", home_phone="", work_phone="", fax="",
                           email_2="", email_3="", email_1="", website="", group_phone="", birth_day="", birth_month="", anniversary_date="",
                           anniversary_month="", anniversary_year="", birth_year="")
    contact.id = app.contact.get_contacts_list()[0].id
    old_contacts = db.get_contact_list()
    app.contact.edit_first_contact(contact)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact.id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key= Contact.id_or_max) == sorted(app.group.get_contact_list(), key= Contact.id_or_max)