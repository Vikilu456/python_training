from model.group import Group
from model.contact import Contact
import random

def test_add_contact_to_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            lastname="lName"
        ))

    # получаем данные из базы для выбора random контакта и присоединения к random группе
    list_contacts = db.get_contact_list()
    list_groups = db.get_group_list()
    contact = random.choice(list_contacts)
    group = random.choice(list_groups)
    # выполняем присоединение random контакта к random группе
    app.contact.add_contact_to_group(contact.id, group.id)
    # берем из базы данные о контактах в группах
    db_contacts = db.get_contacts_in_group()
    assert list(filter(lambda x: x.group_id == int(group.id), db_contacts)) == sorted(app.contact.get_contact_list_from_group_page(group.id), key=Group.id_or_max)
