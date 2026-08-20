from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import Session


class Database:

    def __init__(self, main_db, sql_loader, attachments=None):

        self.loader = sql_loader

        self.engine = create_engine(
            f"sqlite:///{main_db}",
            future=True
        )

        attachments = attachments or {}

        @event.listens_for(self.engine, "connect")
        def attach_databases(dbapi_connection, connection_record):

            dbapi_connection.create_function(
                "CASEFOLD",
                1,
                lambda s: s.casefold() if s is not None else None
            )

            dbapi_connection.create_function(
                "ULOWER",
                1,
                lambda s: s.lower() if s is not None else None
            )

            dbapi_connection.create_function(
                "UUPPER",
                1,
                lambda s: s.upper() if s is not None else None
            )

            cursor = dbapi_connection.cursor()

            for alias, db in attachments.items():
                cursor.execute(
                    f"ATTACH DATABASE '{db}' AS {alias}"
                )

            cursor.close()

#    def query(self, file, sql_args=None, params=None):
#
#        sql = self.loader.render(
#            file,
#            **(sql_args or {})
#        )


#        with Session(self.engine) as session:

#            result = session.execute(
#                text(sql),
#                params or {}
#            )

#            rows = result.mappings().all()

#            return [dict(row) for row in rows]

#    def query_one(self, file, sql_args=None, params=None):

#        sql = self.loader.render(
#            file,
#            **(sql_args or {})
#        )

#        with Session(self.engine) as session:

#            result = session.execute(
#                text(sql),
#                params or {}
#            )

#            row = result.mappings().first()

#            return dict(row) if row else None

#    def scalar(self, file, sql_args=None, params=None):

#        sql = self.loader.render(
#            file,
#            **(sql_args or {})
#        )


#        with Session(self.engine) as session:

#            result = session.execute(
#                text(sql),
#                params or {}
#            )

#            return result.scalar()

#    def execute(self, file, sql_args=None, params=None):

#        sql = self.loader.render(
#            file,
#            **(sql_args or {})
#        )


#        with Session(self.engine) as session:

#            session.execute(
#                text(sql),
#                params or {}
#            )

#            session.commit()
