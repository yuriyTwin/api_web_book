from sqlalchemy import text
from sqlalchemy.orm import Session


class QueryResult:

    def __init__(self, database, sql_file, params):
        self.database = database
        self.sql_file = sql_file
        self.params = params

    @property
    def sql(self):
        sql_text = self.database.loader.render(self.sql_file)
        return sql_text

    def one(self):
        with Session(self.database.engine) as session:
            result = session.execute(text(self.sql), self.params)
            row = result.mappings().first()
            return dict(row) if row else None

    def all(self):
        with Session(self.database.engine) as session:
            result = session.execute(text(self.sql), self.params)
            return [dict(r) for r in result.mappings().all()]

    def scalar(self):
        with Session(self.database.engine) as session:
            return session.execute(text(self.sql), self.params).scalar()

    def exec(self):
        with Session(self.database.engine) as session:
            session.execute(text(self.sql), self.params)
            session.commit()
