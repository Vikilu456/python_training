import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook")
            for row in cursor:
                (id, firstname, lastname, address) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Contact(id=str(id), group_id=group_id))
        finally:
            cursor.close()
        return list

    def db_count_address_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Contact(id=str(id), group_id=group_id))
        finally:
            cursor.close()
        return len(list)

    def destroy(self):
        self.connection.close()
