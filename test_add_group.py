# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


class AddNewGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()
# MAIN TEST
    def test_add_new_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.create_new_group(Group(name="new group", header="group header", footer="group footer"))
        self.app.logout()




    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
