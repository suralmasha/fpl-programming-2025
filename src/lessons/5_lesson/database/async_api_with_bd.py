# pip install databases aiosqlite / poetry add databases aiosqlite
# databases - асинхронный доступ к БД
# aiosqlite - драйвер SQLite для async

from contextlib import asynccontextmanager

import databases
import sqlalchemy
from fastapi import FastAPI, HTTPException

from .data_models import DBUser
from .db_utils import DATABASE_URL

# создаем объект базы
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# определяем таблицу
users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
)

# создаем движок SQLAlchemy и создаем таблицу в БД
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001 - особенности FastAPI
    """Функция, реализующая контекст загрузки FastAPI."""
    await database.connect()  # подключение к базе при старте сервера
    yield
    await database.disconnect()  # отключение базы при завершении сервера


app = FastAPI()


@app.get('/users')
async def read_users():
    """GET /users — получить всех пользователей"""
    query = users.select()
    return await database.fetch_all(query)


@app.post('/users')
async def create_user(user: DBUser):
    """POST /users — добавить пользователя"""
    query = users.insert().values(name=user.name)
    user_id = await database.execute(query)
    return {'id': user_id, 'name': user.name}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    """DELETE /users/{user_id} — удалить пользователя по id"""
    query = users.delete().where(users.c.id == user_id)
    deleted = await database.execute(query)
    if deleted == 0:
        raise HTTPException(status_code=404, detail='User not found')
    return {'status': 'deleted', 'id': user_id}


@app.delete('/users')
async def delete_all_users():
    """DELETE /users — очистить всю таблицу"""
    query = users.delete()
    await database.execute(query)
    return {'status': 'all users deleted'}


"""
read_users:
curl http://127.0.0.1:8000/users

create_user:
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d '{"name": "Alice"}'
`user` здесь не строка, а Pydantic модель -> нужен POST-запрос с JSON в теле запроса

delete_user:
curl -X DELETE "http://127.0.0.1:8000/users/7"

delete_all_users:
curl -X DELETE "http://127.0.0.1:8000/users"
"""
