# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(
        firstname="Fname",
        middlename= "mName",
        lastname="lName",
        nickname="nickname",
        title="title",
        company="company",
        address="adress",
        home="+79999999999",
        email="mail@mail.ru",
        byear="1988"
    ))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(
        firstname="",
        middlename="",
        lastname="",
        nickname="",
        title="",
        company="",
        address="",
        home="",
        email="",
        byear=""
    ))
    app.session.logout()