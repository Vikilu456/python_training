from model.contact import Contact
import random


def test_modify_name_data(app, db, json_contacts, check_ui, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            lastname="lName"
        ))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data = json_contacts
    app.contact.modify_contact_by_id(contact_data, contact.id)
    assert len(old_contacts) == app.contact.count()
    old_contacts[old_contacts.index(contact)] = contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(db.get_contact_list(), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
