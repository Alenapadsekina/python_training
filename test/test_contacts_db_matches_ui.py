from model.contact import Contact

def test_contacts_list(app, db):
    ui_contact_list = app.contact.get_contacts_list()
    def clean(contact):
        return Contact(id = contact.id, first_name= contact.first_name.strip(), last_name= contact.last_name.strip(), address_1= contact.address_1,
                       all_emails_from_contact_page=contact.all_emails_from_contact_page, all_phones_from_contact_page=contact.all_phones_from_contact_page)
    db_contact_list = map(clean, db.get_contact_list())
    assert sorted(ui_contact_list, key=Contact.id_or_max) == sorted(db_contact_list, key=Contact.id_or_max)