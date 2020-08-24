
# DELETE 1ST CONTACT
def test_delete_1st_contact(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()