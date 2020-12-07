from model.group import Group
import random


def test_modify_group(app, json_groups, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_data = Group(name="11", header="22", footer="33")
    app.group.modify_group_by_id(group_data, group.id)
    assert len(old_groups) == app.group.count()
    old_groups[old_groups.index(group)] = group_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_group_list(), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
