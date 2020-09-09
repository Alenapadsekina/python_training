# -*- coding: utf-8 -*-
from model.group import Group


# EDIT 1ST GROUP
def test_edit_first_group(app):
    group = Group(name="the edited name", header="edited header", footer="edited footer")
    if app.group.count()==0:
        app.group.create_gr(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)==len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)




