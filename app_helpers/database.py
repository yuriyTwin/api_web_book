from pathlib import Path
from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import Session
from .sql_loader import SqlLoader


class Database:

    def __init__(self, main_db, sql_dir, attachments=None):
        """
        Args:
            main_db: путь к основной БД
            sql_dir: директория с SQL шаблонами
            attachments: словарь подключаемых БД
        """
        # Инициализируем лоадер здесь
        self.loader = SqlLoader(sql_dir)
        
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
