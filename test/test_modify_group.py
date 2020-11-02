from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Group2", header="Group2Header", footer="Group2Comment"))
    app.session.logout()
