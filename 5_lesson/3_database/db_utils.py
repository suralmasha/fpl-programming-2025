import sqlite3

DB_FILE = 'test.db'
DATABASE_URL = 'sqlite:///./test.db'

# Создание таблицы
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")
conn.commit()
conn.close()


def get_users():
    """Получить всех пользователей."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'name': r[1]} for r in rows]


def add_user(name: str):
    """Добавить пользователя."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
