from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, email=None, email2=None, email3=None, byear=None, id=None, homephone=None,
                 mobilephone=None,
                 workphone=None, secondaryphone=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 all_emails_from_view_page=None, group_id=None, all_emails_from_db=None, all_phones_from_db=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_emails_from_view_page = all_emails_from_view_page
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.email, self.email2)

    # def __repr__(self):
    #     return "%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
    #     self.id, self.firstname, self.address, self.email, self.email2, self.email3,
    #     self.homephone, self.mobilephone, self.workphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname, self.lastname == other.lastname, self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
