# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [
#     Contact(firstname=firstname, lastname=lastname, address=address,
#             homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
#             email=email, email2=email2, email3=email3)
#     for firstname in ["", random_string("firstname", 10)]
#     for lastname in ["", random_string("lastname", 10)]
#     for address in ["", random_string("address", 50)]
#     for homephone in ["", random_string("homephone", 12)]
#     for mobilephone in ["", random_string("mobilephone", 12)]
#     for workphone in ["", random_string("workphone", 12)]
#     for secondaryphone in ["", random_string("secondaryphone", 12)]
#     for email in ["", random_string("email", 20)]
#     for email2 in ["", random_string("email2", 20)]
#     for email3 in ["", random_string("email3", 20)]
#
# ]

testdata = [Contact(firstname="", lastname="", address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    email="", email2="", email3="")] + [
               Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
                       address=random_string("address", 50),
                       homephone=random_string("homephone", 12), mobilephone=random_string("mobilephone", 12),
                       workphone=random_string("workphone", 12),
                       secondaryphone=random_string("secondaryphone", 12),
                       email=random_string("email", 20), email2=random_string("email2", 20),
                       email3=random_string("email3", 20)) for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

