from model.contact import Contact

def test_modify_name_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            middlename="mName",
            lastname="lName",
        ))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="new_Fname",
        middlename="new_mName",
        lastname="new_lName",
    )
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_adress_data(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(
#             address="adress",
#         ))
#     app.contact.edit_first_contact(Contact(
#         address="new_adress"
#     ))

