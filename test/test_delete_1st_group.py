from model.group import Group

# DELETE 1ST GROUP
def test_delete_1st_group(app):
    if app.group.count() == 0:
        app.group.create_gr(Group(name="new group", header="group header", footer="group footer"))
        print("NO GROUPS")
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[0:1]=[]
    assert old_groups == new_groups