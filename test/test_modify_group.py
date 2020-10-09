# -*- coding: utf-8 -*-
from model.group import Group
import random


# MODIFY GROUP NAME
def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_gr(Group(name="new group", header="group header", footer="group footer"))
        print("NO GROUPS")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_id = group.id
    app.group.modify_group_by_id(Group(name="MODIFIED GROUP NAME"), group.id)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == group_id:
            old_groups[i].name = "MODIFIED GROUP NAME"
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)