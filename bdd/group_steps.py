from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given('a new group with <name>, <header>, <footer>', target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create_gr(new_group)


@then ('the new group list is equal to the old group list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#Scenario: Modify a group
@given ('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list())==0:
        app.group.create_gr(Group(name="name", header="header", footer="footer"))
    return db.get_group_list()

@given ('a random group from the list', target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when ('I modify the group <name> from the list')
def modified_group(app, name, random_group):
    return app.group.modify_group_by_id(Group(name=name), random_group.id)

@then ('the new group list is equal to the old group list with the modified group')
def verify_group_modified(db, random_group, non_empty_group_list, name, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == random_group.id:
            old_groups[i].name = name
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#Scenario: Delete a group
@given ('a non-empty group list', target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list())==0:
        app.group.create_gr(Group(name="name", header="header", footer="footer"))
    return db.get_group_list()

@given ('a random group from the list', target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when ('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then ('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, random_group, non_empty_group_list, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)