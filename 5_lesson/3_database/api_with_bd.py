from fastapi import FastAPI

from .db_utils import add_user, get_users

"""
Всегда лучше отделять логику работы с базой в отдельные функции (get_users, add_user) или модули (db_utils),
чтобы код был чистым и читаемым

Модуль `sqlite3` синхронный. Для асинхронного апи используют `databases`
"""

app = FastAPI()


@app.get('/users')
def read_users():
    return get_users()


@app.post('/users')
def create_user(name: str):
    add_user(name)
    return {'status': 'ok', 'name': name}


"""
read_users:
curl http://127.0.0.1:8000/users

create_user:
curl -X POST "http://127.0.0.1:8000/users?name=Bob"
"""
