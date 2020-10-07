from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

db = ORMFixture(host="127.0.0.1", name = "addressbook", user = "root", password = "")

#try:
#    l = db.get_contacts_not_in_group(Group(id='81'))
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#    db.destroy()
#    pass

try:
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
#    index = randrange(len(old_contacts))
    new_contact_lastname = Contact(last_name="New last name")
#    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(new_contact_lastname, contact.id)
 #   assert len(old_contacts) == app.contact.count()
  #  new_contacts = db.get_contact_list()
  #  old_contacts[index].last_name = contact.last_name
  #  assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    print(contact)
finally:
    pass
