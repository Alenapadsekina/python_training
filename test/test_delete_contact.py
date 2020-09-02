
# DELETE 1ST CONTACT
def test_delete_1st_contact(app):
    app.contact.delete_first_contact()
    app.session.logout()