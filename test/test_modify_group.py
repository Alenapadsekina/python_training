# -*- coding: utf-8 -*-
from model.group import Group


# MODIFY GROUP NAME
def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name"))


# MODIFY GROUP HEADER
def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
