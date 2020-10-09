# -*- coding: utf-8 -*-
from model.group import Group


# EDIT 1ST GROUP
def test_edit_first_group(app, db, check_ui):
    group = Group(name="EDITED NAME", header="EDITED HEADER", footer="EDITED FOOTER")
    if app.group.count()==0:
        app.group.create_gr(Group(name="name", header="header", footer="footer"))
    group.id = app.group.get_group_list()[0].id
    old_groups = db.get_group_list()
    app.group.edit_first_group(group)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == group.id:
            old_groups[i] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key= Group.id_or_max) == sorted(app.group.get_contact_list(), key= Group.id_or_max)