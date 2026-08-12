from functools import lru_cache
from .query_result import QueryResult


class SqlRepository:

    def __init__(self, db, folder):

        self.db = db
        self.folder = folder

    @lru_cache(maxsize=None)
    def __getattr__(self, method):

        def execute(**params):

            return QueryResult(
                self.db,
                f"{self.folder}/{method}.sql",
                params
            )

        return execute
