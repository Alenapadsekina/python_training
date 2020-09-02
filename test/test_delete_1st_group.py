from model.group import Group

# DELETE 1ST GROUP
def test_delete_1st_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="new group", header="group header", footer="group footer"))
    app.group.delete_first_group()
