# -*- coding: utf-8 -*-
from model.contact import Contact

# MODIFY 1ST CONTACT NAME
def test_modify_contact_name(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New first name"))
    app.session.logout()
