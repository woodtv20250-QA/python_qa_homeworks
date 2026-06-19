from SubjectTable import Subject_Table
from faker import Faker

fake = Faker()
db = Subject_Table(
    "postgresql://postgres:WoodTV-2026_@localhost:5432/mydatabase")


def test_insert():
    fake_id = fake.random_int(min=100, max=999)
    fake_title = fake.word()

    db.insert(fake_id, fake_title)
    result = db.get_by_id(fake_id)

    assert result is not None
    assert result.subject_title == fake_title

    db.delete(fake_id)
    result = db.get_by_id(fake_id)
    assert result is None


def test_update():
    fake_id = fake.random_int(min=100, max=999)
    fake_title = fake.word()
    db.insert(fake_id, fake_title)

    new_title = fake.word()
    db.update(fake_id, new_title)
    result = db.get_by_id(fake_id)
    assert result.subject_title == new_title

    db.delete(fake_id)


def test_delete():
    fake_id = fake.random_int(min=100, max=999)
    fake_title = fake.word()
    db.insert(fake_id, fake_title)

    db.delete(fake_id)
    result = db.get_by_id(fake_id)
    assert result is None
