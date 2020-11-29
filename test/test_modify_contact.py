from model.contact import Contact
from random import randrange

def test_modify_name_data(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            middlename="mName",
            lastname="lName",
        ))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contacts
    contact.id = old_contacts[0].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

