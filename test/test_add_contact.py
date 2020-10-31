# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
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
    app.contact.create(Contact(
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