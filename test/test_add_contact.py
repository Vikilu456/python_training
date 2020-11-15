# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
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
    )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(
#         firstname="",
#         middlename="",
#         lastname="",
#         nickname="",
#         title="",
#         company="",
#         address="",
#         home="",
#         email="",
#         byear=""
#     )
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert old_contacts == new_contacts