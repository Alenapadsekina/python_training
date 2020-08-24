

# DELETE 1ST GROUP
def test_delete_1st_group(app):
    app.navigation.open_groups_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()