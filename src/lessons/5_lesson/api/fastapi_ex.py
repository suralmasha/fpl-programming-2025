from fastapi import FastAPI

from .data_models import Item, User

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello'}


@app.get('/ping')
async def ping():
    return {'message': 'pong'}


@app.get('/greet')
async def greet(name: str = 'anonymous', age: int | None = None):
    """GET-эндпоинт с параметрами"""
    return {'message': f'Hello, {name}!', 'received_age': age}


"""
`name: str = 'anonymous'` - query-параметр с дефолтом
`age: int | None` - необязательный параметр

Path-параметр - часть пути URL, например /items/{item_id}
Query-параметр - после ?, не влияет на путь, передаёт дополнительные данные:
    - ? - начало query-параметров
    - & - разделяет несколько параметров
    - ключ=значение - конкретный параметр

Пример запроса:
http://127.0.0.1:8000/greet?name=Alex&age=30

Или через curl:
curl "http://127.0.0.1:8000/search?q=python&page=2"
"""


"""
Напишите GET-эндпоинт /sum, который принимает два числа и возвращает их сумму:
http://127.0.0.1:8000/sum?a=2&b=5 -> {"sum":7}
"""


@app.post('/user')
async def create_user(user: User):  # Модель User определяет схему JSON
    """
    POST-эндпоинт (когда клиент отправляет данные, обычно в виде JSON)

    Создание ресурса (несколько одинаковых запросов -> несколько ресурсов)
    """
    return {'status': 'ok', 'received': user, 'message': f'User {user.name} is {user.age} years old.'}


"""
Запрос можно отправить через Swagger -> Try it out

Или через curl:
curl -X POST "http://127.0.0.1:8000/user" \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "age": 25}'

`-X POST` - указываем метод
`-H "Content-Type: application/json"` - говорим серверу, что тело JSON
`-d '{"name": "Alice", "age": 25}'` - само тело запроса
"""


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    """
    PUT-эндпоинт

    Обновляет существующий ресурс или создаёт его, если еще нет
    """
    return {'item_name': item.name, 'item_id': item_id}


"""
Запрос можно отправить через Swagger -> Try it out

Или через curl:
curl -X POST "http://127.0.0.1:8000/items/123" \
  -H "Content-Type: application/json" \
  -d '{"name": "Banana", "price": 100, "is_offer": true}'
"""
