# -*- coding: utf-8 -*-
from model.group import Group


# ADD A NEW GROUP
def test_edit_first_group(app):
    app.navigation.open_groups_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited name", header="edited header", footer="edited footer"))
    app.session.logout()