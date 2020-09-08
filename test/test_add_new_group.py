# -*- coding: utf-8 -*-
from model.group import Group


# ADD A NEW GROUP
def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_group(Group(name="new group", header="group header", footer="group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)


# ADD EMPTY GROUP
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
