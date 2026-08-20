from sqlalchemy import text
from sqlalchemy.orm import Session


class QueryResult:

    def __init__(self, database, sql_file, params):
        self.database = database
        self.sql_file = sql_file
        self.params = params
        self._sql = None

    @property
    def sql(self):
        if self._sql is None:
            self._sql = self.database.loader.render(self.sql_file)
        return self._sql

    def _execute_query(self):
        """Вспомогательный метод для выполнения запроса"""
        with Session(self.database.engine) as session:
            return session.execute(text(self.sql), self.params)

    def one(self):
        result = self._execute_query()
        row = result.mappings().first()
        return dict(row) if row else None

    def all(self):
        result = self._execute_query()
        return [dict(r) for r in result.mappings().all()]

    def scalar(self):
        return self._execute_query().scalar()

    def exec(self):
        with Session(self.database.engine) as session:
            session.execute(text(self.sql), self.params)
            session.commit()
