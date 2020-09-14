# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


# MODIFY GROUP NAME
def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New name")
    group.id = old_groups[index].id
    if app.group.count()==0:
        app.group.create_gr(group)
    app.group.modify_group_by_index(group, index)
    assert len(old_groups)==app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


# MODIFY GROUP HEADER
#def test_modify_group_header(app):
#    group = Group(name="name", header="header", footer="footer")
#    if app.group.count()==0:
#        app.group.create_gr(group)
#    app.group.modify_first_group(Group(header="New header"))
