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
    if db.db_count_address_in_groups() == 0:
        list_contacts = db.get_contact_list()
        list_groups = db.get_group_list()
        contact = random.choice(list_contacts)
        group = random.choice(list_groups)
        app.contact.add_contact_to_group(contact.id, group.id)


    # получаем данные из базы для выбора random группы, в которой есть контакты
    list_groups_from_contacts = db.get_contacts_in_group()
    random_group = random.choice(list_groups_from_contacts)
    # выполняем удаление random контакта, содержавшегося в random группе
    app.contact.delete_contact_from_group(random_group.id, str(random_group.group_id))
    assert list(filter(lambda x: x.group_id == int(random_group.group_id), db.get_contacts_in_group())) == sorted(
        app.contact.get_contact_list_from_group_page(str(random_group.group_id)), key=Group.id_or_max)