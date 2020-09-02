# -*- coding: utf-8 -*-
from model.group import Group


# ADD A NEW GROUP
def test_add_new_group(app):
    app.group.create_new_group(Group(name="new group", header="group header", footer="group footer"))
    app.session.logout()


# ADD EMPTY GROUP
#def test_add_empty_group(app):
#    app.group.create_new_group(Group(name="", header="", footer=""))
#    app.session.logout()
