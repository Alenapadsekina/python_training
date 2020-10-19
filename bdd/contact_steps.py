from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contacts list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()

@given('a new contact with <first_name>, <last_name>', target_fixture="new_contact")
def new_contact(first_name, last_name):
    return Contact(first_name=first_name, last_name=last_name)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create_new_contact(new_contact)


@then ('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#Scenario: Modify a contact
@given ('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list())==0:
        app.contact.create_new_contact(Contact(first_name="FN", last_name="LN"))
    return db.get_contact_list()

@given ('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when ('I modify the contact <first_name> from the list')
def modified_contact(app, first_name, random_contact):
    return app.contact.modify_contact_by_id(Contact(first_name=first_name), random_contact.id)

@then ('the new contact list is equal to the old contact list with the modified contact')
def verify_contact_modified(db, random_contact, non_empty_contact_list, first_name, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == random_contact.id:
            old_contacts[i].first_name = first_name
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

#Scenario: Delete a contact
@given ('a non-empty contact list', target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list())==0:
        app.contact.create_new_contact(Contact(first_name="FN", last_name="LN"))
    return db.get_contact_list()

@given ('a random contact from the list', target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when ('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then ('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, random_contact, non_empty_contact_list, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)