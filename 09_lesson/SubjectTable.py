from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Subject_Table:
    scripts = {
        "insert": text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        "delete": text("delete from subject where subject_id = :id"),
        "update": text(
            "update subject set subject_title = :title where subject_id = :id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string, echo=True)

    def get_by_id(self, id):
        sql = text("SELECT * FROM subject WHERE subject_id = :id")
        return self.db.execute(sql, id=id).fetchone()

    def insert(self, id, title):
        self.db.execute(self.scripts["insert"], id=id, title=title)

    def update(self, id, title):
        self.db.execute(self.scripts["update"], id=id, title=title)

    def delete(self, id):
        self.db.execute(self.scripts["delete"], id=id)
