from model.group import Group

# DELETE 1ST GROUP
def test_delete_1st_group(app):

    if app.group.count() == 0:
        app.group.create_new_group(Group(name="new group", header="group header", footer="group footer"))
        print("NO GROUPS")
    else:
        old_groups = app.group.get_group_list()
        app.group.delete_first_group()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups)-1 == len(new_groups)