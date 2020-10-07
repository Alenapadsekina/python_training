# -*- coding: utf-8 -*-
from model.group import Group
import random


# MODIFY GROUP NAME
def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_gr(Group(name="new group", header="group header", footer="group footer"))
        print("NO GROUPS")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(Group(name="New name"), group.id)
    old_groups.remove(group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


# MODIFY GROUP HEADER
#def test_modify_group_header(app):
#    group = Group(name="name", header="header", footer="footer")
#    if app.group.count()==0:
#        app.group.create_gr(group)
#    app.group.modify_first_group(Group(header="New header"))
