# -*- coding: utf-8 -*-
from model.group import Group


# ADD A NEW GROUP
def test_edit_first_group(app):
    if app.group.count()==0:
        app.group.create_new_group(Group(name="name", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="edited name", header="edited header", footer="edited footer"))
