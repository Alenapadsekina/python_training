from model.group import Group
from random import randrange

# DELETE 1ST GROUP
def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create_gr(Group(name="new group", header="group header", footer="group footer"))
        print("NO GROUPS")
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups)-1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1]=[]
    assert old_groups == new_groups