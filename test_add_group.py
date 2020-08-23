# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# MAIN TEST
def test_add_new_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="new group", header="group header", footer="group footer"))
    app.logout()

def tearDown(self):
    app.destroy()
