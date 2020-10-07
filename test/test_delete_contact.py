from model.contact import Contact
import random

# DELETE 1ST CONTACT
def test_delete_1st_contact(app, db, check_ui):
    if len(db.get_contact_list())==0:
        app.contact.create_new_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
                    company="some_company", address_1="123 Tice Blvd.", mobile_phone="2013912500",
                    address_2="Woodcliff Lake", home_phone="2013912501", work_phone="2013912502", fax="2013912503",
                    email_2="test.email.2@test.com", email_3="test.email.3@test.com",
                    email_1="test.email.1@test.com", website="http://homepage.com", group_phone="8885016953",
                    birth_day="17", birth_month="February", anniversary_date="18",
                    anniversary_month="December", anniversary_year="1990", birth_year="1990"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max)==sorted(new_contacts, key=Contact.id_or_max)


#    if check_ui:
#        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)