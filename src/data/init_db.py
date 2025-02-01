"""
Инициализация базы данных SQLite3
"""
import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

from decouple import config

DB_NAME: str = config("DB_NAME", cast=str)

conn: Connection | None = None
cur: Cursor | None = None


def get_db(name: str | None = None, reset: bool = False):
    """Подключение к файлу БД SQLite"""
    global conn, cur

    if conn:
        if not reset:
            return
        conn = None

    if not name:
        base_dir = Path(__file__).resolve().parent.parent
        db_name: str = config("DB_NAME", cast=str)
        name = os.getenv(
            "CRYPТID_SQLIТE_DB",
            default=os.path.join(base_dir, db_name)
        )

    conn = connect(name, check_same_thread=False)
    cur = conn.cursor()


get_db()
