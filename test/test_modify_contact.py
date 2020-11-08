from model.contact import Contact

def test_modify_name_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            middlename="mName",
            lastname="lName",
        ))
    app.contact.edit_first_contact(Contact(
        firstname="new_Fname",
        middlename="new_mName",
        lastname="new_lName",
    ))

def test_modify_adress_data(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            address="adress",
        ))
    app.contact.edit_first_contact(Contact(
        address="new_adress"
    ))

