# -*- coding: utf-8 -*-
from model.group import Group


# MODIFY GROUP NAME
def test_modify_group_name(app):
    if app.group.count()==0:
        app.group.create_new_group(Group(name="name", header="header", footer="footer"))
    app.group.modify_first_group(Group(name="New name"))


# MODIFY GROUP HEADER
def test_modify_group_header(app):
    if app.group.count()==0:
        app.group.create_new_group(Group(name="name", header="header", footer="footer"))
    app.group.modify_first_group(Group(header="New header"))
