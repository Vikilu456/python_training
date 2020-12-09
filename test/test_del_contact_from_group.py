from model.group import Group
from model.contact import Contact
import random

def test_delete_contact_to_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            lastname="lName"
        ))

    group = random.choice(db.get_group_list())
    free_contact = random.choice(db.get_contacts_in_group(Group(id=str(group.id))))
    if not free_contact:
        free_contact = random.choice(db.get_contacts_not_in_group(Group(id=str(group.id))))
        app.contact.add_contact_to_group(free_contact.id, group.id)

    app.contact.delete_contact_from_group(free_contact.id, group.id)
    assert sorted(db.get_contacts_in_group(Group(id=str(group.id))), key=Contact.id_or_max) == sorted(
        app.contact.get_contact_list_from_group_page(group.id), key=Contact.id_or_max)
