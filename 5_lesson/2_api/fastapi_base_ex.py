# pip install "fastapi[standard]" "uvicorn[standard]" / poetry add "fastapi[standard]" "uvicorn[standard]"

from fastapi import FastAPI

app = FastAPI()  # Создаем приложение


@app.get('/')  # Декоратор, который превращает функцию в эндпоинт
async def root():
    """Корневой эндпоинт"""
    return {'message': 'hello'}


@app.get('/ping')
async def ping():
    """Базовый эндпоинт для проверки доступности сервиса"""
    return {'message': 'pong'}


"""
`fastapi dev` - утилита fastapi-cli
    - под капотом поднимает Uvicorn в режиме разработки
    - включает слежения за изменениями для автоматического перезапуска (hot reload)
    - режим разработки

`fastapi run`
    - нет слежения за изменениями и автоматического перезапуска
    - максимально приближено к production

`fastapi dev main.py` = `uvicorn main:app --reload`  (`main` - имя модуля, `app` - имя переменной)
`fastapi run main.py` = `uvicorn main:app`

Пример запроса:
    - Найти сервис в браузере: http://127.0.0.1:8000/
    - Открыть документацию: http://127.0.0.1:8000/docs

Или через curl:
curl -X GET http://127.0.0.1:8000/  # `-X GET` - метод запроса (GET по умолчанию, поэтому можно не указывать)
curl http://127.0.0.1:8000/
"""
