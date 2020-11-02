from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(
        firstname="new_Fname",
        middlename="new_mName",
        lastname="new_lName",
        nickname="new_nickname",
        title="new_title",
        company="new_company",
        address="new_adress",
        home="+78888888888",
        email="new_mail@mail.ru",
        byear="1985"
    ))
    app.session.logout()
