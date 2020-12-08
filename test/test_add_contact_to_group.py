from model.group import Group
from model.contact import Contact
import random

def test_add_contact_to_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    # выбрали случайную группу
    group = random.choice(db.get_group_list())
    # проверили наличие "свободных контактов" вне выбранной группы, создали новый контакт, если "свободных" нет
    if not db.get_contacts_not_in_group(Group(id=str(group.id))):
        app.contact.create(Contact(
            firstname="Fname",
            lastname="lName"
        ))
    # случайно выбрали из списка, несодержащихся в группе контактов, один контакт
    contact = random.choice(db.get_contacts_not_in_group(Group(id=str(group.id))))
    # добавили случайный контакт в группу, в которой его нет
    app.contact.add_contact_to_group(contact.id, group.id)
    assert sorted(db.get_contacts_in_group(Group(id=str(group.id))), key=Group.id_or_max) == sorted(
        app.contact.get_contact_list_from_group_page(group.id), key=Group.id_or_max)
