from model.contact import Contact
import re


def test_base_info_on_home_page(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="Fname",
            lastname="lName",
            address="address address 2",
            email="email@test.te",
            email2="email2@test.te",
            email3="email3@test.te",
            homephone="+7111111111",
            mobilephone="+7222222222",
            workphone="+7333333333",
            secondaryphone="+7444444444"
        ))

    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    count = 0
    for contact in contacts_from_home_page:
        assert contact.firstname == contacts_from_db[count].firstname
        assert contact.lastname == contacts_from_db[count].lastname
        assert contact.address == contacts_from_db[count].address
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[count])
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[count])
        count += 1


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
